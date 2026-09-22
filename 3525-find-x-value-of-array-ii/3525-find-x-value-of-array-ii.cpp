#include <vector>

using namespace std;

class Solution {
    struct Node {
        int remain[5] = {0};
        int prod = 1;
        bool is_empty = false;
    };

    int n, k;
    vector<Node> tree;

    Node merge(const Node& left, const Node& right) {
        if (left.is_empty) return right;
        if (right.is_empty) return left;

        Node parent;
        parent.prod = (left.prod * right.prod) % k;
        
        for (int r = 0; r < k; ++r) {
            parent.remain[r] = left.remain[r];
        }
        for (int r = 0; r < k; ++r) {
            int new_rem = (r * left.prod) % k;
            parent.remain[new_rem] += right.remain[r];
        }
        return parent;
    }

    void build(const vector<int>& nums, int cur, int lo, int hi) {
        if (lo == hi) {
            int val = nums[lo] % k;
            tree[cur].remain[val] = 1;
            tree[cur].prod = val;
            return;
        }
        int mid = lo + (hi - lo) / 2;
        build(nums, 2 * cur + 1, lo, mid);
        build(nums, 2 * cur + 2, mid + 1, hi);
        tree[cur] = merge(tree[2 * cur + 1], tree[2 * cur + 2]);
    }

    void update(int cur, int lo, int hi, int idx, int val) {
        if (lo == hi) {
            int v = val % k;
            for (int r = 0; r < k; ++r) {
                tree[cur].remain[r] = 0;
            }
            tree[cur].remain[v] = 1;
            tree[cur].prod = v;
            return;
        }
        int mid = lo + (hi - lo) / 2;
        if (idx <= mid) {
            update(2 * cur + 1, lo, mid, idx, val);
        } else {
            update(2 * cur + 2, mid + 1, hi, idx, val);
        }
        tree[cur] = merge(tree[2 * cur + 1], tree[2 * cur + 2]);
    }

    Node query(int cur, int lo, int hi, int ql, int qr) {
        if (ql <= lo && hi <= qr) {
            return tree[cur];
        }
        int mid = lo + (hi - lo) / 2;
        if (qr <= mid) {
            return query(2 * cur + 1, lo, mid, ql, qr);
        }
        if (ql > mid) {
            return query(2 * cur + 2, mid + 1, hi, ql, qr);
        }
        Node left = query(2 * cur + 1, lo, mid, ql, qr);
        Node right = query(2 * cur + 2, mid + 1, hi, ql, qr);
        return merge(left, right);
    }

public:
    vector<int> resultArray(vector<int>& nums, int k_val, vector<vector<int>>& queries) {
        n = nums.size();
        k = k_val;
        tree.assign(4 * n, Node());

        build(nums, 0, 0, n - 1);

        vector<int> ans;
        ans.reserve(queries.size());

        for (const auto& q : queries) {
            int idx = q[0];
            int val = q[1];
            int start = q[2];
            int x = q[3];

            update(0, 0, n - 1, idx, val);
            Node res = query(0, 0, n - 1, start, n - 1);
            ans.push_back(res.remain[x]);
        }

        return ans;
    }
};
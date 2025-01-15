"""
721. Accounts Merge

Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.
Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, 
they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.
After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. 
The accounts themselves can be returned in any order.

Example 1:

Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

Example 2:
Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]

Constraints:
1 <= accounts.length <= 1000
2 <= accounts[i].length <= 10
1 <= accounts[i][j].length <= 30
accounts[i][0] consists of English letters.
accounts[i][j] (for j > 0) is a valid email.
"""
from typing import List
from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adjList = defaultdict(list)
        mergedAccounts = []
        seen = set()

        def dfs(primary, emails):
            seen.add(primary)
            emails.append(primary)
            for secondary in adjList[primary]:
                if secondary not in seen:
                    dfs(secondary, emails)

        for account in accounts:
            primary = account[1]
            if not adjList[primary]:
                pass
            for secondary in account[2:]:
                adjList[primary].append(secondary)
                adjList[secondary].append(primary)

        for account in accounts:
            name, primary = account[0], account[1]
            if primary not in seen:
                emails = []
                dfs(primary, emails)
                emails.sort()
                mergedAccounts.append([name] + emails)

        return mergedAccounts


sol = Solution()
print(sol.accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))
print(sol.accountsMerge([["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]])) # failed testcase


"""
Very good explanation in editorial:

Here, we will represent emails as nodes, and an edge will signify that two emails are connected and hence belong to the same person. 
This means that any two emails that are connected by a path of edges must also belong to the same person. Initially, we are given N accounts, where each account's emails make up a connected component.
Our first step should be to ensure that for each account, all of its nodes are connected. Suppose an account has K emails, and we want to connect these emails. Since all emails in an account are connected, 
we can add an edge between every pair of emails. This will create a complete subgraph and require adding (KC2) edges. However, do we really need that many edges to keep track of which emails belong to the same account? 
No, as long as two emails are connected by a path of edges, we know they belong to the same account. So instead of creating a complete subgraph for each account, we can create an acyclic graph using only K−1 edges. 
Recall that K−1 is the minimum number of edges required to connect K nodes. In this approach, we will connect emails in an account in a star manner with the first email as the internal node of the star and all other emails as the leaves (as shown below).

The beauty of connecting the emails in each account in this manner is that after connecting an email to a second account, that email will have one edge going to an email in the first account 
and one edge going to an email in the second account. Thereby automatically merging the two accounts. The below slideshow depicts the merging process for four accounts that belong to two different people.

After iterating over each account and connecting the emails as described above, we will have a one or more connected components. Each connected component will represent one person, 
and the nodes in the connected component are the person's emails. Now our task is to explore each connected component to find all the emails that belong to each person. 
Since a depth-first search is guaranteed to explore every node in a connected component, we will perform a DFS on each connected component (person) to find all of the connected emails.

To do so, we will iterate over all of the nodes and consider starting a DFS. If the node has already been visited, in an earlier DFS, we will not start a DFS. 
Otherwise, perform a DFS traversal over the connected component and store all the visited emails together, as they all belong to one person. Each time we visit an email during a DFS,
we will mark it as visited to ensure that we do not search the same connected component more than once. To read more about how DFS can be leveraged to find components you can refer to the first approach here.

Algorithm:
Create an adjacency list: For each account add an edge between the first email (accountFirstEmail) and each of the other emails in the account.
Traverse over the accounts; for each account, check if the first email in the account (accountFirstEmail) was already visited. If so, then do not start a new DFS. Otherwise, perform DFS with this email as the source node.
During each DFS, store the traversed emails in an array mergedAccount, also mark all these emails as visited.
After the DFS traversal is over, sort the emails and add the account name (accountName) at the start of the vector mergedAccount.
Store the vector mergedAccount in the answer list mergedAccounts.

Time complexity: O(NK logNK)
In the worst case, all the emails will end up belonging to a single person. The total number of emails will be N*K, and we need to sort these emails. 
DFS traversal will take NK operations as no email will be traversed more than once.
"""

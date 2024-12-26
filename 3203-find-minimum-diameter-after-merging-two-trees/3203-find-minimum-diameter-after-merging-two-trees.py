class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        adj_list_1 = defaultdict(list)
        adj_list_2 = defaultdict(list)

        for source, dest in edges1:
            adj_list_1[source].append(dest)
            adj_list_1[dest].append(source)

        for source, dest in edges2:
            adj_list_2[source].append(dest)
            adj_list_2[dest].append(source)

        def find_diameter(adj_list: dict) -> int:
            if not adj_list:
                return 0

            q = deque()
            q.append(0)

            last_visited = None
            visited = defaultdict(bool)
            while(q):
                len_q = len(q)
                for i in range(len_q):
                    curr = q.popleft()
                    visited[curr] = True
                    last_visited = curr
                    for neighbor in adj_list[curr]:
                        if not visited[neighbor]:
                            q.append(neighbor)

            visited = defaultdict(bool)
            q.append(last_visited)
            dist = -1
            while(q):
                len_q = len(q)
                for i in range(len_q):
                    curr = q.popleft()
                    visited[curr] = True
                    for neighbor in adj_list[curr]:
                        if not visited[neighbor]:
                            q.append(neighbor)

                dist += 1
            return dist

        diameter_1 = 0
        diameter_2 = 0

        if adj_list_1:
           diameter_1 = find_diameter(adj_list_1)

        if adj_list_2:
           diameter_2 = find_diameter(adj_list_2)



        return max(diameter_1, diameter_2, ceil(diameter_1/2) + ceil(diameter_2/2) + 1)
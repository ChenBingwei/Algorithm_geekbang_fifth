import datetime
import heapq
from typing import List


class Text_List_Node:
    def __init__(self, tweetId, userId, next=None):
        self.tweetId = tweetId
        self.userId = userId
        self.time = datetime.datetime.now()
        self.next = next

    def __lt__(self, other):
        return self.time > other.time


class Twitter:

    def __init__(self):
        self.user_follow_map = {}
        self.user_tweet_map = {}
        # 提前模拟用户注册
        for i in range(1, 501):
            self.user_follow_map.setdefault(i, {i})
            self.user_tweet_map.setdefault(i, None)

    def postTweet(self, userId: int, tweetId: int) -> None:
        new_text_node = Text_List_Node(tweetId, userId)
        tmp = self.user_tweet_map[userId]
        new_text_node.next = tmp
        self.user_tweet_map[userId] = new_text_node

    def getNewsFeed(self, userId: int) -> List[int]:
        priority_queue = []
        news_list = []
        # push follow
        for followed_id in self.user_follow_map.get(userId, []):
            if self.user_tweet_map.get(followed_id):
                heapq.heappush(priority_queue, self.user_tweet_map[followed_id])
        # merge
        while priority_queue:
            latest_new = heapq.heappop(priority_queue)
            news_list.append(latest_new.tweetId)
            if latest_new.next:
                heapq.heappush(priority_queue, latest_new.next)
            if len(news_list) == 10:
                break
        return news_list

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_follow_map.setdefault(followerId, set())
        self.user_follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_follow_map[followerId]:
            self.user_follow_map[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

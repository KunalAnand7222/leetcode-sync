import requests

ku="kunal_codexx"
ana="https://leetcode.com/graphql"

ani={
"query":"""
query getUserProfile($username: String!) {
  matchedUser(username: $username) {
    submitStatsGlobal {
      acSubmissionNum {
        difficulty
        count
      }
    }
  }
}
""",
"variables":{"username":ku}
}

res=requests.post(ana,json=ani).json()
ab=res["data"]["matchedUser"]["submitStatsGlobal"]["acSubmissionNum"]

xy={i["difficulty"]:i["count"] for i in ab}
ani2={
"query":"""
query recentSubmissions($username: String!) {
  recentSubmissionList(username: $username) {
    title
    timestamp
  }
}
""",
"variables":{"username":ku}
}

res2=requests.post(ana,json=ani2).json()

subs=res2["data"]["recentSubmissionList"]

import datetime

today=datetime.datetime.utcnow().date()

count=0
for i in subs:
    t=datetime.datetime.utcfromtimestamp(int(i["timestamp"])).date()
    if t==today:
        count+=1
readme=f"""
<h1 align="center">🚀 Kunal's Coding Dashboard</h1>

<p align="center">
  <img src="https://leetcard.jacoblin.cool/{ku}?theme=dark&font=baloo&ext=contest" />
</p>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=KunalAnand7222&show_icons=true&theme=radical" />
</p>

---

## 📊 LeetCode Breakdown

| Level | Count |
|------|------|
| 🟢 Easy | {xy.get("Easy",0)} |
| 🟡 Medium | {xy.get("Medium",0)} |
| 🔴 Hard | {xy.get("Hard",0)} |

---

## 🔥 Coding Activity
- 🚀 Total Problems Solved: {sum(xy.values())}
- 💡 Focus: Data Structures & Algorithms
- ⚡ Consistency Mode: ON

---

## 🧠 Skills Built
- Dynamic Programming  
- Graph Algorithms  
- Backtracking  
- Union-Find  

---

⭐ Auto-updated daily using GitHub Actions
"""

with open("README.md","w") as f:
    f.write(readme)

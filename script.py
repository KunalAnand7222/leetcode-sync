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

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
<h2 align="center">🚀 Kunal's LeetCode Dashboard</h2>

<p align="center">
  <img src="https://leetcard.jacoblin.cool/{ku}?theme=dark&font=baloo&ext=contest" />
</p>

---

### 📊 Problem Breakdown

- 🟢 Easy: {xy.get("Easy",0)}  
- 🟡 Medium: {xy.get("Medium",0)}  
- 🔴 Hard: {xy.get("Hard",0)}  

---

### ⚡ Consistency
- 🔥 Daily DSA practice  
- 🎯 Focus: Problem Solving + Optimization  
- 🚀 Goal: Crack top product-based companies  

---

### 🧠 Skills from Practice
- Dynamic Programming  
- Graphs & Trees  
- Backtracking  
- Union-Find  

---

⭐ Auto-updated using GitHub Actions
"""

with open("README.md","w") as f:
    f.write(readme)

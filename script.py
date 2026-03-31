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
## 🚀 LeetCode Stats

- Easy: {xy.get("Easy",0)}
- Medium: {xy.get("Medium",0)}
- Hard: {xy.get("Hard",0)}

Updated automatically daily 🔥
"""

with open("README.md","w") as f:
    f.write(readme)

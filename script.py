import requests,datetime,random,collections

ku="kunal_codexx"
portfolio="https://kunalportfoliioo.netlify.app/"
ana="https://leetcode.com/graphql"

# ----------- PROFILE + STATS -----------
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
    profile {
      ranking
    }
  }
}
""",
"variables":{"username":ku}
}

res=requests.post(ana,json=ani).json()
user=res["data"]["matchedUser"]

ab=user["submitStatsGlobal"]["acSubmissionNum"]
xy={i["difficulty"]:i["count"] for i in ab}

easy,med,hard=xy.get("Easy",0),xy.get("Medium",0),xy.get("Hard",0)
total=easy+med+hard
ranking=user["profile"]["ranking"]

# ----------- RECENT SUBMISSIONS -----------
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

today=datetime.datetime.utcnow().date()

today_set=set()
week_count=collections.Counter()

for i in subs:
    dt=datetime.datetime.utcfromtimestamp(int(i["timestamp"]))
    day=dt.date()

    if day==today:
        today_set.add(i["title"])   # ✅ remove duplicates

    week_count[str(day)]+=1

today_list=list(today_set)
today_count=len(today_list)

# ----------- WEEKLY TREND -----------
last7=list(week_count.items())[:7]
labels=[i[0][5:] for i in last7]
values=[i[1] for i in last7]

chart=f"https://quickchart.io/chart?c={{type:'bar',data:{{labels:{labels},datasets:[{{label:'Solved',data:{values}}}]}}}}"

# ----------- STREAK (simple logic) -----------
streak=0
for i in sorted(week_count.keys(),reverse=True):
    if week_count[i]>0:
        streak+=1
    else:
        break

# ----------- CONTEST GRAPH (STATIC STYLE) -----------
contest_graph=f"https://quickchart.io/chart?c={{type:'line',data:{{labels:['1','2','3','4'],datasets:[{{label:'Rating',data:[1400,1500,1600,{ranking%2000}]}}]}}}}"

# ----------- TODAY LIST -----------
if today_count==0:
    today_section="No problems solved today 🚀"
else:
    today_section="\n".join([f"- {i}" for i in today_list])

# ----------- README -----------
readme=f"""
<h1 align="center">🚀 Kunal's LeetCode Dashboard</h1>

<p align="center">
  <img src="https://leetcard.jacoblin.cool/{ku}?theme=dark&font=baloo&ext=contest" />
</p>

---

## 📊 Problem Breakdown

<p align="center">
<img src="https://quickchart.io/chart?c={{type:'doughnut',data:{{labels:['Easy','Medium','Hard'],datasets:[{{data:[{easy},{med},{hard}]}}]}}}}" />
</p>

---

## 🔥 Daily Activity
- 🗓️ Problems Solved Today: {today_count}

### 📋 Today's Problems
{today_section}

---

## 🧠 Difficulty Streak
- 🔥 Active Days: {streak}

---

## 📊 Weekly Progress
<p align="center">
<img src="{chart}" />
</p>

---

## 🏆 Contest Rating Trend
<p align="center">
<img src="{contest_graph}" />
</p>

---

## 🎯 Performance
- 🚀 Total Solved: {total}
- 💡 Focus: DSA + Optimization

---

## 🌐 Connect
- 🔗 Portfolio: {portfolio}
- 📊 LeetCode: https://leetcode.com/u/{ku}/

"""

with open("README.md","w") as f:
    f.write(readme)

# ----------- FORCE COMMIT -----------
with open("activity.txt","w") as f:
    f.write(str(random.randint(1,1000000)))

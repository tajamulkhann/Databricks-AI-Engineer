# 🚀 **CREATE SECRET SCOPE USING UI (STEP-BY-STEP)**

## ✅ **Step 1: Open Databricks Workspace**

You’re already here:
👉 `https://adb.azuredatabricks.net#secrets/list?scope-co`

---

## ✅ **Step 2: Use This Direct UI Path**

### 👉 Option A (Easiest – paste once)

Just paste this in your browser:

```text
https://adb.azuredatabricks.net#secrets/list?scope-co
```

👉 This is the **only way via UI** (Databricks doesn’t expose it in sidebar)

---

## ❗ Important

Databricks **does NOT show Secret Scope in left menu**
So:
👉 This hidden URL is the official UI entry

---

# ✅ **Step 3: Fill Form**

You’ll see a simple form:

### Fill like this:

* **Scope Name** → `coa-scope`
* **Manage Principal** → `All Users` *(for POC)*

Click **Create**

---

# 🔑 **Step 4: Add Secret (Token)**

Now go here:

```text
https://adb.azuredatabricks.net#secrets/list?scope-co
```

Click:
👉 **Add Secret**

Fill:

* **Key** → `db-token`
* **Value** → paste your access token

Click **Save**

---

# 🧠 **Step 5: Use in Notebook**

```python
TOKEN = dbutils.secrets.get("coa-scope", "db-token")
```

---

# ⚠️ **IF YOU CAN’T ACCESS THE PAGE**

Then your org has restrictions.

### You’ll see:

* 403 error
* or page not loading

👉 Then do this:

### Ask your admin:

“Please enable secret scopes or create one for me”

OR use temporary workaround:

```python
TOKEN = "your_token_here"
```

---

# 🔥 QUICK SUMMARY

| Task         | How                     |
| ------------ | ----------------------- |
| Create scope | Hidden URL              |
| Add secret   | Scope page              |
| Use secret   | `dbutils.secrets.get()` |

---

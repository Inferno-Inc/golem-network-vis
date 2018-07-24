
# coding: utf-8

# In[15]:


import pandas as pd


# In[16]:


df = pd.read_csv("./monitor.csv", index_col="node_id")


# In[17]:


d = df.to_dict("index")


# In[18]:


import json
with open("node_info.json", "w") as f:
    json_text = json.dumps(d, ensure_ascii=True)
    f.write("node_info = ")
    f.write(json_text)
    f.write(";")



with open("data.txt", "r") as f:
    d = f.readlines()

d.pop(0)
d.pop(0)

keys = [k.replace("p2pstats.", "")[:-1] for k in d[::2]]
vals = [json.loads(json.loads(v.replace("\\x", "_UNICX_"))) for v in d[1::2]] # SOOOO UGLY
assert len(keys) == len(vals)
network_all = {k: vv["p2p_snapshot"] for k, vv in zip(keys, vals)}


# In[22]:


with open("p2p_info.json", "w") as f:
    json_text = json.dumps(network_all, ensure_ascii=True)
    f.write("p2p_info = ")
    f.write(json_text)
    f.write(";")

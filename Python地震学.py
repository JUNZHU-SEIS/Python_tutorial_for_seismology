# %% [markdown]
# # 下载地震波形

# %%
from obspy import UTCDateTime
from obspy.clients.fdsn.client import Client
client = Client('IRIS')
t = UTCDateTime("2012-12-14T10:36:01.6Z")
st = client.get_waveforms('TA','E42A','*','BH?',t+300,t+400,attach_response=True)
#st.remove_response(output='VEL')
for tr in st:
    print(tr)
    meta = tr.stats
    # 浏览道头信息 (台网名，台站名，通道名，开始时间，采样率)
    print(meta.network, meta.station, meta.channel, meta.starttime, meta.sampling_rate)
# 存储波形数据
st.write('TA.E42A.mseed')

# %% [markdown]
# # 可视化

# %%
def process(st):
    st.detrend('demean');st.detrend('linear')
    st.taper(.05, max_length=5)
    #st.filter('bandpass', freqmin=1, freqmax=15, zerophase=True, corners=2)
    #st.filter('lowpass', freq=1/10, zerophase=True, corners=2)
    st.filter('highpass', freq=1, zerophase=True, corners=2)
    #st.normalize()
    return st

def visualize(st):
    import matplotlib.pyplot as plt
    import numpy as np
    data = np.array([tr.data for tr in st])
    fig,ax = plt.subplots(3,1, sharex=True)
    for i,a in enumerate(ax):
        a.plot(st[i].data, lw=.8, label=st[i].stats.channel)
        a.legend(loc='upper left')
    a.set_xlabel('Time (s)')
    plt.tight_layout()
    plt.savefig('visualization.pdf')
    #plt.show()
    plt.close()

# %%
from obspy import read
st = read('data/TA.E42A.mseed')
st = process(st)
#st.plot()
visualize(st)

# %% [markdown]
# # 推荐阅读
# Obspy文档：https://docs.obspy.org/index.html



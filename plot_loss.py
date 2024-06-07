#读取loss文件
import datetime
import matplotlib.pyplot as plt
f = open('./loss_0.log')
losses =[]
for line in f:
    
    losses.append(float(line.split(' ')[-1].strip("\n")))
try:
    x = list(range(len(losses)))
    fig, ax1 = plt.subplots(1, 1)
    ax1.plot(x, losses, 'r', label='loss')
    ax1.set_xlabel("step")
    ax1.set_ylabel("loss")
    ax1.set_title("Train Loss")
    plt.legend(loc='best')

    plt.legend(loc='best')

    handles1, labels1 = ax1.get_legend_handles_labels()        
    plt.legend(handles1, labels1, loc='upper right')

    fig.subplots_adjust(right=0.8)  # 防止出现保存图片显示不全的情况
    fig.savefig('./loss{}.png'.format(datetime.datetime.now().strftime("%Y%m%d-%H%M%S")))
    plt.close()
    print("successful save loss curve! ")
except Exception as e:
    print(e)
    
                  
print(losses)

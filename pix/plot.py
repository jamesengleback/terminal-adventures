import pandas as pd
import matplotlib.pyplot as plt

def plot(df):
    idx = range(len(df))
    labels = [i[0] for i in df.index]
    plt.bar(idx,df)
    plt.xticks(idx, labels, rotation=70)
    plt.yticks(range(0,21,4),range(0,21,4))
    plt.xlabel('command')
    plt.ylabel('frequency %')
    plt.title('my command frequency')
    plt.savefig('command-frequency.png')

def process(path):
    # process data
    df = pd.read_csv(path, delim_whitespace=True)
    df = df.value_counts().nlargest(30)
    df /= df.sum()
    df *= 100
    return df

def main():
    data = process('commands')
    plot(data)

if __name__ =='__main__':
    main()

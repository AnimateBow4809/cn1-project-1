import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tick
import math

TIME_FOR_EACH_BIT = 1
# STRING_INPUT = ("01100001011001000110110001100001010110010010000001111001011100000111000001100001"
STRING_INPUT = "010001111000"
A = 1


def NRZI(input):
    out = [0]
    flag = -1
    for s in input:
        if s == '0':
            out.append(flag)
        elif s == '1':
            flag *= -1
            out.append(flag)
    out[0] = out[1]
    return out


def Pseudoternary(input):
    out = [0]
    flag = 1
    for s in input:
        if s == '0':
            out.append(flag)
            flag *= -1
        elif s == '1':
            out.append(0)
    out[0] = out[1]
    return out


def DifferntialManchester(input):
    out = [1]
    flag = 1
    for i in range(0, len(input), 1):
        if input[i] == '0':
            out.append(flag * -1)
            flag = flag * -1
            out.append(flag * -1)
            flag = flag * -1
        elif input[i] == '1':
            out.append(flag)
            out.append(flag * -1)
            flag = flag * -1
    out[0] = out[1]
    return out


def ASK(input, a):
    lis = []
    for i in input:
        if (i == '0'):
            for i in range(0, 40):
                lis.append(a)
        else:
            for i in range(0, 40):
                lis.append(1)
    return lis


def NRZa(input):
    lis = [5]
    for i in input:
        if i == '0':
            for i in range(0, 40):
                lis.append(5+np.random.randn())
        else:
            for i in range(0, 40):
                lis.append(-5+np.random.randn())
    lis[0] = lis[1]
    return lis


def IHDB3(input):
    out = [0]
    flag = 1
    number_of_zeros_since_last_subtiutation = 0
    subflag = 3
    for i in range(0, len(input), 1):
        if input[i] == '0':
            out.append(flag)
            flag *= -1
            number_of_zeros_since_last_subtiutation += 1
            subflag -= 1
        elif input[i] == '1':
            preceding = flag * -1
            if subflag <= 0 and input[i - 1] == '1' and input[i - 2] == '1' and input[i - 3] == '1':
                if number_of_zeros_since_last_subtiutation % 2 == 0:
                    out.append(preceding * -1)
                    out[i] = 0
                    out[i - 1] = 0
                    out[i - 2] = preceding * -1
                    number_of_zeros_since_last_subtiutation = 0
                    flag *= -1
                else:
                    out.append(preceding)
                    out[i] = 0
                    out[i - 1] = 0
                    out[i - 2] = 0
                    number_of_zeros_since_last_subtiutation = 0
                subflag = 3
            else:
                out.append(0)
                subflag -= 1

    out[0] = out[1]
    return out


fig, axs = plt.subplots(4, 2)
fig.tight_layout(pad=1.5, h_pad=2, w_pad=2)
axs[0, 0].set_title("NRZI")
axs[0, 1].set_title("Pseudoternary")
axs[1, 0].set_title("DifferntialManchester")
axs[1, 1].set_title("IHDB3")
axs[2, 0].set_title("ASK")
axs[2, 1].set_title("ASK with noise")
axs[3, 0].set_title("NRZ with noise")

NRZ = NRZI(STRING_INPUT)
PSEUDO = Pseudoternary(STRING_INPUT)
MANCHESTER = DifferntialManchester(STRING_INPUT)
IHDB = IHDB3(STRING_INPUT)
Amplitude = ASK(STRING_INPUT, -1)
ASK_with_noise = ASK(STRING_INPUT, 0)
NRZo = NRZa(STRING_INPUT)

YForNRZ = np.arange(0, len(NRZ) * TIME_FOR_EACH_BIT, TIME_FOR_EACH_BIT)
YForNRZo = np.arange(0, len(NRZo) * TIME_FOR_EACH_BIT, TIME_FOR_EACH_BIT)
YForPSEUDO = np.arange(0, len(PSEUDO) * TIME_FOR_EACH_BIT, TIME_FOR_EACH_BIT)
YForIHDB = np.arange(0, len(IHDB) * TIME_FOR_EACH_BIT, TIME_FOR_EACH_BIT)
YForManchester = np.arange(0, len(MANCHESTER) * TIME_FOR_EACH_BIT / 2, TIME_FOR_EACH_BIT / 2)

x = np.linspace(0, len(STRING_INPUT) * TIME_FOR_EACH_BIT, num=len(Amplitude))

# print(DifferntialManchester(STRING_INPUT))

axs[0, 0].step(YForNRZ, NRZ, color="brown")
axs[0, 1].step(YForPSEUDO, PSEUDO, color="blue")
axs[1, 0].step(YForManchester, MANCHESTER, color="red")
axs[1, 1].step(YForIHDB, IHDB, color="green")
axs[3, 0].plot(YForNRZo, NRZo, color="purple")
axs[2, 0].plot(x, np.sin(((2 * math.pi) / TIME_FOR_EACH_BIT) * x) * Amplitude * A, color="cyan")
axs[2, 1].plot(x, np.sin(((2 * math.pi) / TIME_FOR_EACH_BIT) * x) * ASK_with_noise * 2 * A, color="black")

axs[0, 0].xaxis.set_major_locator(tick.MultipleLocator(TIME_FOR_EACH_BIT))
axs[0, 0].xaxis.set_minor_locator(tick.MultipleLocator(TIME_FOR_EACH_BIT))
axs[0, 1].xaxis.set_major_locator(tick.MultipleLocator(TIME_FOR_EACH_BIT))
axs[0, 1].xaxis.set_minor_locator(tick.MultipleLocator(TIME_FOR_EACH_BIT))
axs[1, 0].xaxis.set_major_locator(tick.MultipleLocator(TIME_FOR_EACH_BIT / 2))
axs[1, 0].xaxis.set_minor_locator(tick.MultipleLocator(TIME_FOR_EACH_BIT / 2))
axs[1, 1].xaxis.set_major_locator(tick.MultipleLocator(TIME_FOR_EACH_BIT))
axs[1, 1].xaxis.set_minor_locator(tick.MultipleLocator(TIME_FOR_EACH_BIT))
axs[2, 0].xaxis.set_minor_locator(tick.MultipleLocator(TIME_FOR_EACH_BIT))
axs[2, 0].xaxis.set_major_locator(tick.MultipleLocator(TIME_FOR_EACH_BIT))
axs[2, 1].xaxis.set_minor_locator(tick.MultipleLocator(TIME_FOR_EACH_BIT))
axs[2, 1].xaxis.set_major_locator(tick.MultipleLocator(TIME_FOR_EACH_BIT))
axs[3, 0].xaxis.set_major_locator(tick.MultipleLocator(40))
axs[3, 0].xaxis.set_minor_locator(tick.MultipleLocator(40))

for k in range(0, len(NRZa(STRING_INPUT)) * TIME_FOR_EACH_BIT, 40):
    axs[3, 0].axvline(x=k, linestyle="--", color="dimgrey")

for i in range(0, 3, 1):
    for j in range(0, 2, 1):
        for k in range(0, len(NRZI(STRING_INPUT)) * TIME_FOR_EACH_BIT, 1):
            axs[i, j].axvline(x=k, linestyle="--", color="dimgrey")

plt.show()

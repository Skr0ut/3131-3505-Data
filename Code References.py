## 3505 - A4: Q9
for i, cont in enumerate(contr_levels):
    for j, cond in enumerate(conditions):
        for trial in trials:
            spike_times = df[(df['neuron'] == 'm1_6') & (df['condition'] == cond) & (df['contrast'] == cont) & (df['repetition'] == trial)]['spiketime']
            axs[i, j].vlines(spike_times, trial - 0.4, trial + 0.4)
        axs[i, j].set_yticks(range(0, 10, 2))
        axs[i, 0].set_ylabel(str(cont) + "%" + ' Contrast')
        axs[i, 1].set_ylabel("Trial Num")
        if cond == 'CTRL':
            axs[i, j].axvspan(stim_on_time, stim_off_time, alpha=cont/100, color='grey')
        if cond == 'ADAPT':
            axs[i, j].axvspan(adapt_on_time, adapt_off_time, alpha=.5, color='grey')
            axs[i, j].axvspan(stim_on_time, stim_off_time, alpha=cont/100, color='grey')
        if i == 0:
            axs[i, 0].set_title('CTRL Condition', fontsize=10)
            axs[i, 1].set_title('ADAPT Condition', fontsize=10)
        if i == 9:
            axs[i, 1].set_xlabel('Time\n(Milliseconds)')
            axs[i, 0].set_xlabel('Time\n(Milliseconds)')

def plot_temperatures(paths):
    LogLogs = [f"{path}/LogLog_{t}" for path, t in zip(paths, [900, 1000, 1100, 1600])]

    Cases = ['SuperLubric']
    Temperatures = [900, 1000,1100,1600]
    Label = ['SL']

    fig = plt.figure(figsize=(14, 14))  # Adjust the figsize as needed

    grid = ImageGrid(
        fig,
        111,
        nrows_ncols=(1, 4),  # Display four subplots in a 2x2 grid
        axes_pad=0.5,
        cbar_location="right",
        cbar_mode="single",
        cbar_size="7%",
        cbar_pad=0.25,
    )

    for i, case in enumerate(Cases):
        for j, (t, LogLog) in enumerate(zip(Temperatures, LogLogs)):
            data = np.loadtxt(LogLog, usecols=[1, 2, 3, 4])
            z = data[:, 3]
            z -= np.mean(z)
            z = z.reshape((500, 500))
            im = grid[i * 2 + j].imshow(z, extent=[0, 500, 0, 500], vmax=0, cmap='viridis')
            grid[i * 2 + j].title.set_text('{}-{}K'.format(Label[i], t))

    grid[-1].cax.colorbar(im)
    grid[-1].cax.toggle_label(True)
    #plt.savefig('{}/sl_PES_Si.png'.format(os.getcwd()), format='png', dpi=300, bbox_inches='tight')
    plt.show()

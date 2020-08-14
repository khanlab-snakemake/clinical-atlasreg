from nilearn import plotting
import matplotlib.pyplot as plt


import matplotlib
matplotlib.use('Agg')

html_view = plotting.view_img(stat_map_img=snakemake.input.ref,bg_img=snakemake.input.flo,
                              opacity=0.5,cmap='viridis',dim=-1,
                              symmetric_cmap=False,title='sub-{subject}'.format(**snakemake.wildcards))

html_view.save_as_html(snakemake.output.html)



fig = plt.figure(figsize=(30, 3), facecolor='k')
display = plotting.plot_anat(snakemake.input.ref,figure=fig,dim=0,display_mode='y')
display.add_contours(snakemake.input.flo,colors='r')
display.savefig(snakemake.output.png)
display.close()

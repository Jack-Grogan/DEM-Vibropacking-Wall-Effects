<div align="center">
  <h1 align="center"> DEM-Vibropacking-Wall-Effects </h1>
</div>

This repository provides all the code files used within the paper "Effect of Cylinder Wall Parameters on the Final Packing Density of Mono-Disperse Spheres Subject to Three Dimensional Vibrations".

## Code Run Order

The run order of both the shell launch scripts, and the file it launches are outlined below. All drop down directories below can be run without any dependency on files in the other drop down directories. 

<details markdown="1"><summary><h3><a href="./model_validation">model_validation</a></h3></summary>
  
<details markdown="1"><summary><h4><a href="./model_validation/box_plots">box_plots</a></h4></summary>
  
  1\) [launch_continuous_batch_generator.sh](./model_validation/box_plots/launch_continuous_batch_generator.sh) &#8594; [continuous_batch_generator.py](./model_validation/box_plots/continuous_batch_generator.py) <br />
  1\) [launch_continuous_generator.sh](./model_validation/box_plots/launch_continuous_generator.sh) &#8594; [continuous_generator.py](./model_validation/box_plots/continuous_generator.py) <br />
  1\) [launch_continuous_generator_60s.sh](./model_validation/box_plots/launch_continuous_generator_60s.sh) &#8594; [continuous_generator_60s.py](./model_validation/box_plots/continuous_generator_60s.py) <br />
  1\) [launch_periodic_batch_generator.sh](./model_validation/box_plots/launch_periodic_batch_generator.sh) &#8594; [periodic_batch_generator.py](./model_validation/box_plots/periodic_batch_generator.py) <br />
  1\) [launch_periodic_generator.sh](./model_validation/box_plots/launch_periodic_generator.sh) &#8594; [periodic_generator.py](./model_validation/box_plots/periodic_generator.py) <br />
  2\) [final_paper_packing_launch.sh](./model_validation/box_plots/final_paper_packing_launch.sh) &#8594; [final_paper_packing_method.py](./model_validation/box_plots/final_paper_packing_method.py) <br />
  2\) [final_voxel_packing_launch.sh](./model_validation/box_plots/final_voxel_packing_launch.sh) &#8594; [final_voxel_packing_method.py](./model_validation/box_plots/final_voxel_packing_method.py) <br />
  2\) [z_voxel_continuous_packing_launch.sh](./model_validation/box_plots/z_voxel_continuous_packing_launch.sh) &#8594; [z_voxel_continuous_packing_method.py](./model_validation/box_plots/z_voxel_continuous_packing_method.py) <br />
  2\) [z_voxel_periodic_packing_launch.sh](./model_validation/box_plots/z_voxel_periodic_packing_launch.sh) &#8594; [z_voxel_periodic_packing_method.py](./model_validation/box_plots/z_voxel_periodic_packing_method.py) <br />
  2\) [z_voxel_batch_continuous_packing_launch.sh](./model_validation/box_plots/z_voxel_batch_continuous_packing_launch.sh) &#8594; [z_voxel_batch_continuous_packing_method.py](./model_validation/box_plots/z_voxel_batch_continuous_packing_method.py) <br />
  2\) [z_voxel_batch_periodic_packing_launch.sh](./model_validation/box_plots/z_voxel_batch_periodic_packing_launch.sh) &#8594; [z_voxel_batch_periodic_packing_method.py](./model_validation/box_plots/z_voxel_batch_periodic_packing_method.py) <br />
  3\) [graph_launch.sh](./model_validation/box_plots/graph_launch.sh) &#8594; [model_validation_graphs.py](./model_validation/box_plots/model_validation_graphs.py) <br />
  3\) [z_graph_launch.sh](./model_validation/box_plots/z_graph_launch.sh) &#8594; [z_voxels_graph.py](./model_validation/box_plots/z_voxels_graph.py)
  
</details>

<details markdown="1"><summary><h4><a href="./model_validation/line_plots">line_plots</a></h4></summary>
  
<details markdown="1"><summary><h5><a href="./model_validation/line_plots/continuous_graph">continuous_graph</a></h5></summary>
  
  1\) [simulation_launch.sh](./model_validation/line_plots/continuous_graph/simulation_launch.sh)  &#8594; [shake.sim](./model_validation/line_plots/continuous_graph/shake.sim) <br />
  2\) [voxel_packing_launch.sh](./model_validation/line_plots/continuous_graph/voxel_packing_launch.sh) &#8594; [voxel_packing_method.py](./model_validation/line_plots/continuous_graph/voxel_packing_method.py) <br />
  2\) [paper_packing_launch.sh](./model_validation/line_plots/continuous_graph/paper_packing_launch.sh) &#8594; [paper_packing_method.py](./model_validation/line_plots/continuous_graph/paper_packing_method.py) <br />
  3\) [continuous_voxel_graph_launch.sh](./model_validation/line_plots/continuous_graph/continuous_voxel_graph_launch.sh) &#8594; [density_time_continuous_voxel_graph.py](./model_validation/line_plots/continuous_graph/density_time_continuous_voxel_graph.py) <br />
  3\) [continuous_graph_launch.sh](./model_validation/line_plots/continuous_graph/continuous_graph_launch.sh) &#8594; [density_time_continuous_graph.py](./model_validation/line_plots/continuous_graph/density_time_continuous_graph.py)
  
</details>

<details markdown="1"><summary><h5><a href="./model_validation/line_plots/periodic_graph">periodic_graph</a></h5></summary>
  
  1\) [simulation_launch.sh](./model_validation/line_plots/periodic_graph/simulation_launch.sh) &#8594; [shake.sim](./model_validation/line_plots/periodic_graph/shake.sim) <br />
  2\) [voxel_packing_launch.sh](./model_validation/line_plots/periodic_graph/voxel_packing_launch.sh) &#8594; [voxel_packing_method.py](./model_validation/line_plots/periodic_graph/voxel_packing_method.py) <br />
  2\) [paper_packing_launch.sh](./model_validation/line_plots/periodic_graph/paper_packing_launch.sh) &#8594; [paper_packing_method.py](./model_validation/line_plots/periodic_graph/paper_packing_method.py) <br />
  3\) [periodic_voxel_graph_launch.sh](./model_validation/line_plots/periodic_graph/periodic_voxel_graph_launch.sh) &#8594;  [density_time_periodic_voxel_graph.py](./model_validation/line_plots/periodic_graph/density_time_periodic_voxel_graph.py) <br />
  3\) [periodic_graph_launch.sh](./model_validation/line_plots/periodic_graph/periodic_graph_launch.sh) &#8594;  [density_time_periodic_graph.py](./model_validation/line_plots/periodic_graph/density_time_periodic_graph.py)
  
</details>
</details>
</details>

<details markdown="1"><summary><h3><a href="./glass_bead_wall_effects">glass_bead_wall_effects</a></h3></summary>

<details markdown="1"><summary><h4><a href="./glass_bead_wall_effects/particle_wall_restitution">particle_wall_restitution</a></h4></summary>

1\) [launch_generator.sh](./glass_bead_wall_effects/particle_wall_restitution/launch_generator.sh) &#8594; [generator.py](./glass_bead_wall_effects/particle_wall_restitution/generator.py)
 <br />
2\) [final_voxel_packing_launch.sh](./glass_bead_wall_effects/particle_wall_restitution/final_voxel_packing_launch.sh) &#8594; [final_voxel_packing_method.py](./glass_bead_wall_effects/particle_wall_restitution/final_voxel_packing_method.py) <br />
2\) [final_paper_packing_launch.sh](./glass_bead_wall_effects/particle_wall_restitution/final_paper_packing_launch.sh) &#8594; [final_paper_packing_method.py](./glass_bead_wall_effects/particle_wall_restitution/final_paper_packing_method.py) <br />
3\) [restitution_voxel_graph_launch.sh](./glass_bead_wall_effects/particle_wall_restitution/restitution_voxel_graph_launch.sh) &#8594; [wall_restitution_voxel_graph.py](./glass_bead_wall_effects/particle_wall_restitution/wall_restitution_voxel_graph.py) <br />
3\) [restitution_graph_launch.sh](./glass_bead_wall_effects/particle_wall_restitution/restitution_graph_launch.sh) &#8594; [wall_restitution_graph.py](./glass_bead_wall_effects/particle_wall_restitution/wall_restitution_graph.py)

</details>

<details markdown="1"><summary><h4><a href="./glass_bead_wall_effects/particle_wall_rolling_friction">particle_wall_rolling_friction</a></h4></summary>

1\) [launch_generator.sh](./glass_bead_wall_effects/particle_wall_restitution/launch_generator.sh) &#8594; [generator.py](./glass_bead_wall_effects/particle_wall_restitution/generator.py) <br />
1\) [launch_generator_wide.sh](./glass_bead_wall_effects/particle_wall_rolling_friction/launch_generator_wide.sh) &#8594; [generator_wide.py](./glass_bead_wall_effects/particle_wall_rolling_friction/generator_wide.py) <br />
2\) [final_voxel_packing_launch.sh](./glass_bead_wall_effects/particle_wall_rolling_friction/final_voxel_packing_launch.sh) &#8594; [final_voxel_packing_method.py](./glass_bead_wall_effects/particle_wall_rolling_friction/final_voxel_packing_method.py) <br />
2\) [final_voxel_packing_launch_wide.sh](./glass_bead_wall_effects/particle_wall_rolling_friction/final_voxel_packing_launch_wide.sh) &#8594; [final_voxel_packing_method_wide.py](./glass_bead_wall_effects/particle_wall_rolling_friction/final_voxel_packing_method_wide.py) <br />
2\) [final_paper_packing_launch.sh](./glass_bead_wall_effects/particle_wall_rolling_friction/final_paper_packing_launch.sh) &#8594; [final_paper_packing_method.py](./glass_bead_wall_effects/particle_wall_rolling_friction/final_paper_packing_method.py) <br />
2\) [final_paper_packing_launch_wide.sh](./glass_bead_wall_effects/particle_wall_rolling_friction/final_paper_packing_launch_wide.sh) &#8594; [final_paper_packing_method_wide.py](./glass_bead_wall_effects/particle_wall_rolling_friction/final_paper_packing_method_wide.py) <br />
3\) [rolling_voxel_graph_launch.sh](./glass_bead_wall_effects/particle_wall_rolling_friction/rolling_voxel_graph_launch.sh) &#8594; [wall_rolling_voxel_graph.py](./glass_bead_wall_effects/particle_wall_rolling_friction/wall_rolling_voxel_graph.py) <br />
3\) [rolling_graph_launch.sh](./glass_bead_wall_effects/particle_wall_rolling_friction/rolling_graph_launch.sh) &#8594; [wall_rolling_graph.py](./glass_bead_wall_effects/particle_wall_rolling_friction/wall_rolling_graph.py)

</details>

<details markdown="1"><summary><h4><a href="./glass_bead_wall_effects/particle_wall_sliding_friction">particle_wall_sliding_friction</a></h4></summary>

1\) [launch_generator.sh](./glass_bead_wall_effects/particle_wall_sliding_friction/launch_generator.sh) &#8594; [generator.py](./glass_bead_wall_effects/particle_wall_sliding_friction/generator.py) <br />
2\) [final_voxel_packing_launch.sh](./glass_bead_wall_effects/particle_wall_sliding_friction/final_voxel_packing_launch.sh) &#8594; [final_voxel_packing_method.py](./glass_bead_wall_effects/particle_wall_sliding_friction/final_voxel_packing_method.py) <br />
2\) [final_paper_packing_launch.sh](./glass_bead_wall_effects/particle_wall_sliding_friction/final_paper_packing_launch.sh) &#8594; [final_paper_packing_method.py](./glass_bead_wall_effects/particle_wall_sliding_friction/final_paper_packing_method.py) <br />
3\) [sliding_voxel_graph_launch.sh](./glass_bead_wall_effects/particle_wall_sliding_friction/sliding_voxel_graph_launch.sh) &#8594; [wall_sliding_voxel_graph.py](./glass_bead_wall_effects/particle_wall_sliding_friction/wall_sliding_voxel_graph.py) <br />
3\) [sliding_graph_launch.sh](./glass_bead_wall_effects/particle_wall_sliding_friction/sliding_graph_launch.sh) &#8594; [wall_sliding_graph.py](./glass_bead_wall_effects/particle_wall_sliding_friction/wall_sliding_graph.py)

</details>

</details>

<details markdown="1"><summary><h3><a href="./method_1_wall_extremes">method_1_wall_extremes</a></h3></summary>

1\) [launch_restitution_generator.sh](./method_1_wall_extremes/launch_restitution_generator.sh) &#8594; [restitution_generator.py](./method_1_wall_extremes/restitution_generator.py) <br />
1\) [launch_rolling_generator.sh](./method_1_wall_extremes/launch_rolling_generator.sh) &#8594; [rolling_generator.py](./method_1_wall_extremes/rolling_generator.py) <br />
1\) [launch_sliding_generator.sh](./method_1_wall_extremes/launch_sliding_generator.sh) &#8594; [sliding_generator.py](./method_1_wall_extremes/sliding_generator.py) <br />
2\) [final_voxel_packing_launch_restitution.sh](./method_1_wall_extremes/final_voxel_packing_launch_restitution.sh) &#8594; [final_voxel_packing_method_restitution.py](./method_1_wall_extremes/final_voxel_packing_method_restitution.py) <br />
2\) [final_voxel_packing_launch_rolling.sh](./method_1_wall_extremes/final_voxel_packing_launch_rolling.sh) &#8594; [final_voxel_packing_method_rolling.py](./method_1_wall_extremes/final_voxel_packing_method_rolling.py) <br />
2\) [final_voxel_packing_launch_sliding.sh](./method_1_wall_extremes/final_voxel_packing_launch_sliding.sh) &#8594; [final_voxel_packing_method_sliding.py](./method_1_wall_extremes/final_voxel_packing_method_sliding.py) <br />
2\) [final_paper_packing_launch_restitution.sh](./method_1_wall_extremes/final_paper_packing_launch_restitution.sh) &#8594; [final_paper_packing_method_restitution.py](./method_1_wall_extremes/final_paper_packing_method_restitution.py) <br />
2\) [final_paper_packing_launch_rolling.sh](./method_1_wall_extremes/final_paper_packing_launch_rolling.sh) &#8594; [final_paper_packing_method_rolling.py](./method_1_wall_extremes/final_paper_packing_method_rolling.py) <br />
2\) [final_paper_packing_launch_sliding.sh](./method_1_wall_extremes/final_paper_packing_launch_sliding.sh) &#8594; [final_paper_packing_method_sliding.py](./method_1_wall_extremes/final_paper_packing_method_sliding.py) <br />
3\) [restitution_voxel_graph_launch.sh](./method_1_wall_extremes/restitution_voxel_graph_launch.sh) &#8594; [restitution_voxel_graphs.py](./method_1_wall_extremes/restitution_voxel_graphs.py) <br />
3\) [rolling_voxel_graph_launch.sh](./method_1_wall_extremes/rolling_voxel_graph_launch.sh) &#8594; [rolling_voxel_graphs.py](./method_1_wall_extremes/rolling_voxel_graphs.py) <br />
3\) [sliding_voxel_graph_launch.sh](./method_1_wall_extremes/sliding_voxel_graph_launch.sh) &#8594; [sliding_voxel_graphs.py](./method_1_wall_extremes/sliding_voxel_graphs.py) <br />
3\) [restitution_graph_launch.sh](./method_1_wall_extremes/restitution_graph_launch.sh) &#8594; [restitution_packing_graphs.py](./method_1_wall_extremes/restitution_packing_graphs.py) <br />
3\) [rolling_graph_launch.sh](./method_1_wall_extremes/rolling_graph_launch.sh) &#8594; [rolling_packing_graphs.py](./method_1_wall_extremes/rolling_packing_graphs.py) <br />
3\) [sliding_graph_launch.sh](./method_1_wall_extremes/sliding_graph_launch.sh) &#8594; [sliding_packing_graphs.py](./method_1_wall_extremes/sliding_packing_graphs.py)

</details>

<details markdown="1"><summary><h3><a href="./method_2_wall_extremes">method_2_wall_extremes</a></h3></summary>

1\) [launch_restitution_generator.sh](./method_2_wall_extremes/launch_restitution_generator.sh) &#8594; [restitution_generator.py](./method_2_wall_extremes/restitution_generator.py) <br />
1\) [launch_rolling_generator.sh](./method_2_wall_extremes/launch_rolling_generator.sh) &#8594; [rolling_generator.py](./method_2_wall_extremes/rolling_generator.py) <br />
1\) [launch_sliding_generator.sh](./method_2_wall_extremes/launch_sliding_generator.sh) &#8594; [sliding_generator.py](./method_2_wall_extremes/sliding_generator.py) <br />
2\) [final_voxel_packing_launch_restitution.sh](./method_2_wall_extremes/final_voxel_packing_launch_restitution.sh) &#8594; [final_voxel_packing_method_restitution.py](./method_2_wall_extremes/final_voxel_packing_method_restitution.py) <br />
2\) [final_voxel_packing_launch_rolling.sh](./method_2_wall_extremes/final_voxel_packing_launch_rolling.sh) &#8594; [final_voxel_packing_method_rolling.py](./method_2_wall_extremes/final_voxel_packing_method_rolling.py) <br />
2\) [final_voxel_packing_launch_sliding.sh](./method_2_wall_extremes/final_voxel_packing_launch_sliding.sh) &#8594; [final_voxel_packing_method_sliding.py](./method_2_wall_extremes/final_voxel_packing_method_sliding.py) <br />
2\) [final_paper_packing_launch_restitution.sh](./method_2_wall_extremes/final_paper_packing_launch_restitution.sh) &#8594; [final_paper_packing_method_restitution.py](./method_2_wall_extremes/final_paper_packing_method_restitution.py) <br />
2\) [final_paper_packing_launch_rolling.sh](./method_2_wall_extremes/final_paper_packing_launch_rolling.sh) &#8594; [final_paper_packing_method_rolling.py](./method_2_wall_extremes/final_paper_packing_method_rolling.py) <br />
2\) [final_paper_packing_launch_sliding.sh](./method_2_wall_extremes/final_paper_packing_launch_sliding.sh) &#8594; [final_paper_packing_method_sliding.py](./method_2_wall_extremes/final_paper_packing_method_sliding.py) <br />
3\) [restitution_voxel_graph_launch.sh](./method_2_wall_extremes/restitution_voxel_graph_launch.sh) &#8594; [restitution_voxel_graphs.py](./method_2_wall_extremes/restitution_voxel_graphs.py) <br />
3\) [rolling_voxel_graph_launch.sh](./method_2_wall_extremes/rolling_voxel_graph_launch.sh) &#8594; [rolling_voxel_graphs.py](./method_2_wall_extremes/rolling_voxel_graphs.py) <br />
3\) [sliding_voxel_graph_launch.sh](./method_2_wall_extremes/sliding_voxel_graph_launch.sh) &#8594; [sliding_voxel_graphs.py](./method_2_wall_extremes/sliding_voxel_graphs.py) <br />
3\) [restitution_graph_launch.sh](./method_2_wall_extremes/restitution_graph_launch.sh) &#8594; [restitution_packing_graphs.py](./method_2_wall_extremes/restitution_packing_graphs.py) <br />
3\) [rolling_graph_launch.sh](./method_2_wall_extremes/rolling_graph_launch.sh) &#8594; [rolling_packing_graphs.py](./method_2_wall_extremes/rolling_packing_graphs.py) <br />
3\) [sliding_graph_launch.sh](./method_2_wall_extremes/sliding_graph_launch.sh) &#8594; [sliding_packing_graphs.py](./method_2_wall_extremes/sliding_packing_graphs.py)

</details>

<details markdown="1"><summary><h3><a href="./method_3_wall_extremes">method_3_wall_extremes</a></h3></summary>

1\) [launch_restitution_generator.sh](./method_3_wall_extremes/launch_restitution_generator.sh) &#8594; [restitution_generator.py](./method_3_wall_extremes/restitution_generator.py) <br />
1\) [launch_rolling_generator.sh](./method_3_wall_extremes/launch_rolling_generator.sh) &#8594; [rolling_generator.py](./method_3_wall_extremes/rolling_generator.py) <br />
1\) [launch_sliding_generator.sh](./method_3_wall_extremes/launch_sliding_generator.sh) &#8594; [sliding_generator.py](./method_3_wall_extremes/sliding_generator.py) <br />
2\) [final_voxel_packing_launch_restitution.sh](./method_3_wall_extremes/final_voxel_packing_launch_restitution.sh) &#8594; [final_voxel_packing_method_restitution.py](./method_3_wall_extremes/final_voxel_packing_method_restitution.py) <br />
2\) [final_voxel_packing_launch_rolling.sh](./method_3_wall_extremes/final_voxel_packing_launch_rolling.sh) &#8594; [final_voxel_packing_method_rolling.py](./method_3_wall_extremes/final_voxel_packing_method_rolling.py) <br />
2\) [final_voxel_packing_launch_sliding.sh](./method_3_wall_extremes/final_voxel_packing_launch_sliding.sh) &#8594; [final_voxel_packing_method_sliding.py](./method_3_wall_extremes/final_voxel_packing_method_sliding.py) <br />
2\) [final_paper_packing_launch_restitution.sh](./method_3_wall_extremes/final_paper_packing_launch_restitution.sh) &#8594; [final_paper_packing_method_restitution.py](./method_3_wall_extremes/final_paper_packing_method_restitution.py) <br />
2\) [final_paper_packing_launch_rolling.sh](./method_3_wall_extremes/final_paper_packing_launch_rolling.sh) &#8594; [final_paper_packing_method_rolling.py](./method_3_wall_extremes/final_paper_packing_method_rolling.py) <br />
2\) [final_paper_packing_launch_sliding.sh](./method_3_wall_extremes/final_paper_packing_launch_sliding.sh) &#8594; [final_paper_packing_method_sliding.py](./method_3_wall_extremes/final_paper_packing_method_sliding.py) <br />
3\) [restitution_voxel_graph_launch.sh](./method_3_wall_extremes/restitution_voxel_graph_launch.sh) &#8594; [restitution_voxel_graphs_batch.py](./method_3_wall_extremes/restitution_voxel_graphs_batch.py) <br />
3\) [rolling_voxel_graph_launch.sh](./method_3_wall_extremes/rolling_voxel_graph_launch.sh) &#8594; [rolling_voxel_graphs_batch.py](./method_3_wall_extremes/rolling_voxel_graphs_batch.py) <br />
3\) [sliding_voxel_graph_launch.sh](./method_3_wall_extremes/sliding_voxel_graph_launch.sh) &#8594; [sliding_voxel_graphs_batch.py](./method_3_wall_extremes/sliding_voxel_graphs_batch.py) <br />
3\) [restitution_graph_launch.sh](./method_3_wall_extremes/restitution_graph_launch.sh) &#8594; [restitution_packing_graphs_batch.py](./method_3_wall_extremes/restitution_packing_graphs_batch.py) <br />
3\) [rolling_graph_launch.sh](./method_3_wall_extremes/rolling_graph_launch.sh) &#8594; [rolling_packing_graphs_batch.py](./method_3_wall_extremes/rolling_packing_graphs_batch.py) <br />
3\) [sliding_graph_launch.sh](./method_3_wall_extremes/sliding_graph_launch.sh) &#8594; [sliding_packing_graphs_batch.py](./method_3_wall_extremes/sliding_packing_graphs_batch.py)

</details>

<details markdown="1"><summary><h3><a href="./method_4_wall_extremes">method_4_wall_extremes</a></h3></summary>

1\) [launch_restitution_generator.sh](./method_4_wall_extremes/launch_restitution_generator.sh) &#8594; [restitution_generator.py](./method_4_wall_extremes/restitution_generator.py) <br />
1\) [launch_rolling_generator.sh](./method_4_wall_extremes/launch_rolling_generator.sh) &#8594; [rolling_generator.py](./method_4_wall_extremes/rolling_generator.py) <br />
1\) [launch_sliding_generator.sh](./method_4_wall_extremes/launch_sliding_generator.sh) &#8594; [sliding_generator.py](./method_4_wall_extremes/sliding_generator.py) <br />
2\) [final_voxel_packing_launch_restitution.sh](./method_4_wall_extremes/final_voxel_packing_launch_restitution.sh) &#8594; [final_voxel_packing_method_restitution.py](./method_4_wall_extremes/final_voxel_packing_method_restitution.py) <br />
2\) [final_voxel_packing_launch_rolling.sh](./method_4_wall_extremes/final_voxel_packing_launch_rolling.sh) &#8594; [final_voxel_packing_method_rolling.py](./method_4_wall_extremes/final_voxel_packing_method_rolling.py) <br />
2\) [final_voxel_packing_launch_sliding.sh](./method_4_wall_extremes/final_voxel_packing_launch_sliding.sh) &#8594; [final_voxel_packing_method_sliding.py](./method_4_wall_extremes/final_voxel_packing_method_sliding.py) <br />
2\) [final_paper_packing_launch_restitution.sh](./method_4_wall_extremes/final_paper_packing_launch_restitution.sh) &#8594; [final_paper_packing_method_restitution.py](./method_4_wall_extremes/final_paper_packing_method_restitution.py) <br />
2\) [final_paper_packing_launch_rolling.sh](./method_4_wall_extremes/final_paper_packing_launch_rolling.sh) &#8594; [final_paper_packing_method_rolling.py](./method_4_wall_extremes/final_paper_packing_method_rolling.py) <br />
2\) [final_paper_packing_launch_sliding.sh](./method_4_wall_extremes/final_paper_packing_launch_sliding.sh) &#8594; [final_paper_packing_method_sliding.py](./method_4_wall_extremes/final_paper_packing_method_sliding.py) <br />
3\) [restitution_voxel_graph_launch.sh](./method_4_wall_extremes/restitution_voxel_graph_launch.sh) &#8594; [restitution_voxel_graphs.py](./method_4_wall_extremes/restitution_voxel_graphs.py) <br />
3\) [rolling_voxel_graph_launch.sh](./method_4_wall_extremes/rolling_voxel_graph_launch.sh) &#8594; [rolling_voxel_graphs.py](./method_4_wall_extremes/rolling_voxel_graphs.py) <br />
3\) [sliding_voxel_graph_launch.sh](./method_4_wall_extremes/sliding_voxel_graph_launch.sh) &#8594; [sliding_voxel_graphs.py](./method_4_wall_extremes/sliding_voxel_graphs.py) <br />
3\) [restitution_graph_launch.sh](./method_4_wall_extremes/restitution_graph_launch.sh) &#8594; [restitution_packing_graphs.py](./method_4_wall_extremes/restitution_packing_graphs.py) <br />
3\) [rolling_graph_launch.sh](./method_4_wall_extremes/rolling_graph_launch.sh) &#8594; [rolling_packing_graphs.py](./method_4_wall_extremes/rolling_packing_graphs.py) <br />
3\) [sliding_graph_launch.sh](./method_4_wall_extremes/sliding_graph_launch.sh) &#8594; [sliding_packing_graphs.py](./method_4_wall_extremes/sliding_packing_graphs.py)

</details>

## Citing
Please cite the accompanying paper:
> Jack R. Grogan, Andrei L. Nicuşan, Christopher R.K. Windows-Yule, Effect of cylinder wall parameters on the final packing density of mono-disperse spheres subject to three dimensional vibrations, Particuology, 2024

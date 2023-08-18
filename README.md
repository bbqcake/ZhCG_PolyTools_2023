# ZhCG_PolyTools

Updated to work with maya 2023. Sourced from https://www.highend3d.com/maya/script/zhcg_polytools-for-maya-54377
Thanks to [impivot](https://github.com/impivot) for finding bugs with Edit Facets and fixing them.
Thanks to [Mech_Addict](https://polycount.com/profile/Mech_Addict) for testing and finding bugs.

Current known issue:
Edit Component > Spin can give unexpected results when selecting verts. For now please select edges.

All credit to the original Author:
ZhCG
zhcg6740411@gmail.com

# Installation

Download zhcg_polyTools.py and place it in your scripts directory

`C:\Users\USERNAME\Documents\maya\scripts`

If you do not have a userSetup.mel add this file to the same directory.


If you already have a userSetup.mel edit it and add this line:

`python("import maya.cmds as mc; import zhcg_polyTools");`

Start maya and zhcg_polyTools should show up in the menu bar.

# A few features:
Average line:

![](https://i.imgur.com/NjPfuKp.gif)

Shape line:

![](https://i.imgur.com/BAH6KXy.gif)

Randomize:

![](https://i.imgur.com/PHw2pAc.gif)

Relax:

![](https://i.imgur.com/jcP8tWN.gif)

Shrink wrap:

![](https://i.imgur.com/bPMMtVt.gif)

and many more:

![](https://i.imgur.com/uGUiNBP.png)

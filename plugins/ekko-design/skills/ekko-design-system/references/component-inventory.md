# Component inventory

> Generated from Figma "[Ekko UI] - Design System" (export 2026-10-26). DO NOT EDIT — run scripts/build_tokens.py

Every component set in the Figma library with its properties. Variant options are
separated by `/`; BOOLEAN, TEXT and INSTANCE_SWAP are toggles, text and icon slots.
`key` is the Figma component-set key (use it with `importComponentSetByKeyAsync`).


## Avatar

- **Avatar**: **Size**: xs/sm/md/lg/xl; **Type**: Image/Text; **Status**: On/Off; **Shape**: Rounded/Squared  
  `key: fb0ff0e270c76b8ce19586dddf4af46568c6aacc`
- **Avatar stack**: **Quantity**: 2/6/5/4/3; **Size**: xs/sm/md/lg/xl; **Counter**: On/Off  
  `key: 43307b36883cd3edfdb4f6c8988df6a804787563`

## Alert

- **Alert (item)**: **Button count**: 2/1  
  `key: acb9b3e12b1812a342d4346e645c93dd70a151a0`
- **Alert**: **Button**: BOOLEAN; **Title**: BOOLEAN; **Icon**: BOOLEAN; **Close button**: BOOLEAN; **Color**: Grey/Brand/Green/Yellow/Red  
  `key: 7da7b6daf051dc5425ef70bd9f53b2d57ec52917`

## Button

- **Button**: **Icon left**: BOOLEAN; **❖ Icon left**: INSTANCE_SWAP; **Icon right**: BOOLEAN; **❖ Icon right**: INSTANCE_SWAP; **Content**: TEXT; **Size**: xl/lg/md/sm; **Type**: Brand/Secondary/Success/Alert/Clear; **State**: Default/Hover/Focus/Disable; **Text**: On/Off; **Dropdown**: Off/On  
  `key: 591da65a5217e503e3ef3f5fed40d8cad6d767fb`
- **Social button**: **Size**: lg/md/sm; **Type**: Apple/Google/Figme; **State**: Default/Hover/Focus/Disable; **Text**: On/Off  
  `key: 292d84b019ccacdfbdf8ce38f64a0646fb24d8f1`
- **Text link**: **Icon left**: BOOLEAN; **❖ Icon left**: INSTANCE_SWAP; **Icon right**: BOOLEAN; **❖ Icon right**: INSTANCE_SWAP; **Content**: TEXT; **Size**: sm/md/lg/xl; **Type**: Brand/Secondary; **State**: Default/Hover/Focus/Disable; **Text**: On/Off; **Dropdown**: On/Off  
  `key: 0730af2a9d99f1a8a5da37f5929ffc2653dc9051`
- **Button group (item)**: **Icon left**: BOOLEAN; **❖ Icon left**: INSTANCE_SWAP; **Icon right**: BOOLEAN; **❖ Icon right**: INSTANCE_SWAP; **Content**: TEXT; **Size**: lg/md/sm; **State**: Default/Hover/Disable; **Dropdown**: Off/On; **Text**: On/Off; **Checkbox**: Off/On  
  `key: 57ce88458cf824ab034fd44214e49785847bccd1`
- **Group button**: **Size**: lg/md/sm; **Quantity**: 6/5/4/3/2  
  `key: 1fc8830e1a2f29366f6c6c37b9aedc3d76b3eb9e`

## Badge & Chip

- **Badge**: **Size**: lg/md/sm; **Color**: Brand/Green/Yellow/Red/Grey; **Dot**: On/Off; **Icon**: Off/On; **Outline**: On/Off  
  `key: 8963054dc9e4703fa409349365ff98aded37fe0f`
- **Close**: **State**: Default/Hover  
  `key: 57ced888e4a430e77276cb1d227a1eca9fc5ad91`
- **Chip**: **Size**: sm/lg/md; **Color**: Brand/Green/Yellow/Red/Grey; **State**: Default/Hover; **Outline**: On/Off  
  `key: 4b0bb62afdc2dd64ff8d1e49781c857f5e699c74`

## Breadcrumb

- **Breadcrumb (Item)**: **Icon**: BOOLEAN; **Text**: BOOLEAN; **Content**: TEXT; **State**: Default/Hover/Selected  
  `key: 632b756070b5225e621e9b313309d8ba2f5060a0`
- **Breadcrumb**: **Style**: Chevron/Slash; **Quantity**: 4/3/2/1  
  `key: 24711a3bbcaa74f74a86ca5bcd83d5fd5ef57d64`

## Charts

- **Column Chart**: **Show Legends**: BOOLEAN; **Show Value**: BOOLEAN; **Count**: 1/2/3; **Negative Values**: False  
  `key: 81b98a99ac94ea300f1e6b4f4c170fac9edaaadb`
- **Bar Chart**: **Show Legend**: BOOLEAN; **Count**: 1/2/3; **Sticky Label**: False  
  `key: de265c59c81ec554118d55a5aa894d8316b5559c`
- **Line Chart**: **Show Legend**: BOOLEAN; **Type**: Cumulative/Stacked; **Show Plot Area**: True; **Smooth Line**: True; **Count**: 1/2/3  
  `key: 23ff0fb7ccf7c6797f471e1c008108c09a72e83e`
- **Donut Chart**: **Show Legend**: BOOLEAN; **Show Total Values**: BOOLEAN; **Count**: 2/3/4/5/6; **Legend Align**: Center  
  `key: cde1e7425e41c79f4a6158212ba5c2c0b4ab4270`
- **Pie Chart**: **Show Legend**: BOOLEAN; **Count**: 2/3/4/5/6; **Legend Align**: Center  
  `key: 958873958a799d47dd8ae9a372b2468bfbd19c89`
- **Chart-title**: **Dropdown**: BOOLEAN; **Button**: BOOLEAN; **Type**: Column/Bar/Line/Donut/Pie  
  `key: cd57600ef36ad9097a00fca43dfeddb665abda95`

## Checkbox & Radio

- **Check box**: **State**: Default/Hover/Focus/Selected/Indeterminate/Disable  
  `key: ce6403527c945fccda715b1bbe836182c099036b`
- **Radio**: **State**: Default/Hover/Focus/Selected/Disable  
  `key: 8f957f5225ade405803a66903fe604d9df6a0e0a`
- **Checkbox with label**: **State**: Default/Hover/Focus/Selected/Indeterminate/Disable; **Text side**: Left/Right  
  `key: 0f50e5679dea7b508632d269c438a0b9c72935a8`
- **Radio with label**: **State**: Default/Hover/Focus/Selected/Indeterminate/Disable; **Text side**: Left/Right  
  `key: 7dbd16fb744e70e5d7119b5438ab2b5c31455aaa`

## Divider

- **Divider**: **Type**: Horizontal/Vertical; **Style**: Light/Heavy  
  `key: e6b6f5af42b7e2321cdf88253647460e1c37b194`

## File uploader

- **File uploader**: **State**: Default/Hover/Focus/Error/Disable  
  `key: a99a1f055c65c09b2e8f4f90dd1664854fc4dedb`
- **File progress**: **State**: Error/Uploaded/In progress  
  `key: ddc9bc5c6f4fd924967a9f35d84c79a044a7d5fb`

## Input

- **Input addon**: **Icon left**: BOOLEAN; **❖ Icon left**: INSTANCE_SWAP; **Icon right**: BOOLEAN; **❖ Icon right**: INSTANCE_SWAP; **Text**: BOOLEAN; **Content**: TEXT; **Side**: Right/Left; **Size**: sm/md  
  `key: 8be18d0bec00803440a3161f23b201367232344d`
- **Helper text**: **Icon**: BOOLEAN; **Type**: Error/Helper  
  `key: 9931c74c5c968bca1ff0f81714735a2362bdaaf4`
- **Input**: **Label**: BOOLEAN; **Required (*)**: BOOLEAN; **Helper text**: BOOLEAN; **Input addon left**: BOOLEAN; **Input addon right**: BOOLEAN; **Icon left**: BOOLEAN; **❖ Icon left**: INSTANCE_SWAP; **Icon right**: BOOLEAN; **❖ Icon right**: INSTANCE_SWAP; **Content**: TEXT; **Title**: TEXT; **Size**: sm/md/lg; **State**: Default/Filled/Hover/Focus/Error/Disable/Typing/Tag  
  `key: fa797121c6d3a2d483b5887a5bfe7ba8e19e1014`
- **Text area**: **State**: Disable/Empty/Filled/Hover/Focus/Error  
  `key: ab91e38bbc0667b0f851cd6e27da8f1d000fa23b`
- **Message input**: **State**: Default/Filled/Hover/Focus/Error/Disable  
  `key: 47ccf13877f77b3a53c535f4ed811f9e5c4453c3`

## Menu

- **Shortcut**: **Quantity**: 1/3/2  
  `key: 73c8898f3d390db9ead98b3d05a3a1002d982963`
- **Menu (item)**: **Shortcut**: BOOLEAN; **Icon**: BOOLEAN; **Description**: BOOLEAN; **Time**: BOOLEAN; **Sub-menu**: BOOLEAN; **Type**: Social media/Label/Icon/Avatar/Status dot/Checkbox; **State**: Default/Selected/Hover  
  `key: 8279490bfacc62655acaa8c8bda32af8180c5e75`

## Navigation

- **Sidebar (item)**: **Counter**: BOOLEAN; **Arrow**: BOOLEAN; **❖ Icon**: INSTANCE_SWAP; **Type**: Item/Toggle/Label; **State**: Default/Hover/Selected/Focus; **Icon**: Off/On; **Avatar**: Off/On; **Square**: Off/On; **Workspace**: Off/On; **Text**: On/Off  
  `key: 2644b55fcc3e22bd202237ed78a2b9e30e1749dc`
- **Top bar**: **State**: Logged in/Guest  
  `key: aabe29413b7372e0bf60a24577e74e77cb487758`
- **Counter**: **State**: Default/Hover/Selected/Disable/Focus  
  `key: 9b388e1006e7e194832cd4d638ddab5fcecb1e54`

## Pagination

- **Pagination (item)**: (no properties)  
  `key: 9114c733e5bcc9eb5a1aa868054205a08be76b6e`
- **Pagination**: **Add on left**: BOOLEAN; **Add on right**: BOOLEAN; **Type**: White/Clear  
  `key: ce891a15ab687befa6e9031153e34abf4f24091a`

## Picker

- **Date picker (item)**: **Type**: Date/Label; **State**: Default/Hover/Selected/Focus/Range/Disable  
  `key: da69532e8dc599d69abb6c3257dd6581ed5fed0d`
- **Date picker**: **Type**: Year/Date picker/Range/Month  
  `key: 69c6153804157f2dbcc2ee70145263f856b5344a`

## Scroll bar & Slider

- **Scrollbar - Vertical**: **Page Height**: x 2/x 4/x 8; **Position**: Top/Middle/Bottom  
  `key: e82b9033fccc82f7fd472854cebd98efe25336cd`
- **Scrollbar - Horizontal**: **Page**: 400%/800%/200%; **Position**: Leading/Center/Trailing  
  `key: f9b7f1a2fc582dc6e3d689bbfd4ee4619111ac94`
- **Slider**: **Label left**: BOOLEAN; **Label right**: BOOLEAN; **Icon left**: BOOLEAN; **Icon right**: BOOLEAN; **Value**: 0/25/50/75/100; **Dots**: On/Off  
  `key: ef0f35b6e7129e584490b6746b1822086a7424b0`

## Status dot

- **Status dot (Light)**: **Size**: xs/lg/xl/md/sm; **State**: Online/Busy/Offline/Away; **Status**: On/Off; **Outline**: On/Off  
  `key: baa5826d49282b4d9bfe984d4a9b6f299d2c2fee`

## Loader

- **Loader**: (no properties)  
  `key: d58d2009e5535432fbc69ebb39bab688e455fdbd`

## Table

- **Table (Item)**: **Badge 3**: BOOLEAN; **Badge 2**: BOOLEAN; **Help icon**: BOOLEAN; **Checkbox**: BOOLEAN; **❖ Icon**: INSTANCE_SWAP; **Icon 1**: BOOLEAN; **Icon 2**: BOOLEAN; **Icon 3**: BOOLEAN; **Description**: BOOLEAN; **Type**: Item/Label; **Background color**: White/Grey; **Text**: Off/On; **Text bold**: Off/On; **Avatar**: Off/On; **Avatar stack**: Off/On; **Button**: Off/On; **Badge**: Off/On; **Icon**: Off/On  
  `key: 73759c67f0c0692964ecca15d4cea3ef88bfdadb`

## Tabs

- **Underlined tabs (item)**: **Icon**: BOOLEAN; **❖ Icon**: INSTANCE_SWAP; **Counter**: BOOLEAN; **Content**: TEXT; **State**: Default/Hover/Selected/Focus/Disable  
  `key: 14cae17bc494731162bfe81e240af028c7e187f4`
- **Underlined tabs**: **Quantity**: 6/5/4/3/2/1  
  `key: 85ebcbe90d40ed9f86e8f53a73e01d3aae4432fe`
- **Squared tabs (item)**: **Icon**: BOOLEAN; **❖ Icon**: INSTANCE_SWAP; **Counter**: BOOLEAN; **Content**: TEXT; **State**: Default/Hover/Selected/Focus/Disable  
  `key: 96f9d1e6ae2ba53d3b603bae42c06667831b0d79`
- **Squared tabs**: **Quantity**: 6/5/4/3/2  
  `key: a8ae9fd97019bf0c3943942ff82d7681781edce8`

## Toast

- **Toast**: **Button**: BOOLEAN; **Description**: BOOLEAN; **Title**: BOOLEAN; **Icon**: BOOLEAN; **Color**: Brand/Green/Yellow/Red  
  `key: de52629087dfa4cd70ebdffc91b038d5fe0361a0`

## Toggle

- **Toggle with label**: **State**: Default/Hover/Focus/Disable; **Text side**: Left/Right  
  `key: d58ffc1496aaa7d96425a0fd7860563043bb8c14`
- **Toggle**: **State**: Default/Hover/Focus/Disable; **Active**: On/Off  
  `key: a3e5300185aaec4fde7a07e08802483a71018984`

## Tooltip

- **Tooltip**: **Chevron**: On/Off; **Color**: White/Grey/Payday Blue/Fluores¢ent; **Chevron side**: Right/Left/Center  
  `key: 206e5dd33d9a96aad8eae633ee25aa177b533490`

## Logo

- **Ekko logo**: **Type**: Primary/Secondary/Symbol; **Color**: Amicable Jade/Beyond Blue/Fluores¢ent/Payday Blue  
  `key: 5a4d31b53ab4f4d7cf0349f672cc2669772b5097`

## Cursors

- **Cursors / Pointer**: **Type**: Pointer/Pointer active/Arrow/Grab/Grabbed/Help/Move/Text/Typing (GIF)/ZoomIn/ZoomOut  
  `key: 0d1ca002580a55bb2d0568972430dd70f423878c`
- **Cursors / Resize —  Side**: **Type**: Down/Left/LeftRight/Right/Up/UpDown  
  `key: 130d4dae5d95ca25871f36c3b087b34fe1a023bf`
- **Cursors / Status**: **Type**: Copy/Loading/Not-allowed/Poof/Beachball  
  `key: d739ae2163db225fd5912ba01a1099cc12de4bd8`
- **Cursors / Resize —  Scale**: **Type**: East West/Norht South/North East South West/North West South East  
  `key: 258b61e03a4c19ff55bb3a3f5b21c2a2df75a2ca`
- **Cursors / Resize — Direction**: **Type**: East/North/North East/North West/South/South East/South West/West  
  `key: 0c4c784db56f7fbf8cd2a491934178f74833f37d`
- **Cursors / More**: **Type**: Cell/Cross/Make alias/Text vertical  
  `key: 9a9b85592fb306be1e282c4557894763a024bbde`
- **Cursors / Photo**: **Type**: Screenshot/Screenshot select  
  `key: 786c226c24ac408baf85e11eb7742bb194b8e5ee`

## Page template

- **Title**: **Type**: Style/Type/State/Size/Variation/Color/Shape/Status/Text side/Example/Quantity/Outline/Button/Title/Description/Toggle/Background/Type18  
  `key: 67781722b3dd07c86f4dd21d83ac7431966fec62`


# Visual-Comfort-Analysis-Framework

# Visual Comfort Analysis Based on Urban 3D Models and Street View Images—Taking Nanshan District of Shenzhen City as an Example
# 基于城市三维模型和街景图像的视觉舒适度分析——以深圳市南山区为例

I. Application Background and Objectives
一、 应用背景与目标

With the continuous advancement of urbanization, high-rise buildings are increasingly blocking the sky, natural green spaces are diminishing, and the visible sky is shrinking. Consequently, people's attention to urban visual comfort is growing. They hope to enjoy more comfortable landscapes and lighting during their daily commutes. In recent years, Shenzhen, as a model of a forest city and a garden city, has made unremitting efforts in urban greening. How to better study the distribution of urban visual comfort through big data and new methods, and how to guide future urban planning and construction based on these distributions, have become one of the key focuses of urban planning. Visual comfort in urban spaces has become a crucial factor in improving residents' quality of life and shaping the urban image.
In the era of big data, Baidu Street View, as an important channel for understanding the real urban street scenes, has become a major source of urban big data analysis. Empowered by the recent AI trend, a batch of excellent object segmentation models, represented by Unet, have become important tools for analyzing street objects. By integrating the proportion of objects at different locations with questionnaire analysis, a comprehensive study of how street objects in the real world affect urban visual comfort can be conducted. Additionally, the advent of the machine learning era has injected new vitality into research. Neural networks, decision trees, and other machine learning methods can solve many problems that were previously difficult to address. With excellent classification and integration methods, the random forest model, as an efficient model, can effectively learn various types of feature relationships and provide corresponding prediction results based on new features.
Traditional urban visual comfort analysis often focuses only on simple landscape analysis and neglects the impact of daylighting on visual comfort. Some three-dimensional simulation platforms, such as Cesium, have begun to emerge in the new round of visual analysis. They can realistically simulate the changes in light and shadow in cities, and provide detailed displays of urban spatial layout and building structures. These platforms offer precise spatial data for visual comfort analysis and can be integrated into related research as an excellent visualization method.
This study integrates the factors of daylighting and street object segmentation in visual comfort. It uses the random forest model to obtain people's comprehensive perception scores for street object distribution and cumulative daylighting through questionnaires, thereby predicting the comfort distribution across the entire city. Furthermore, it conducts linear-scale spatial interpolation on streets and explores the distribution patterns in traffic zones across the city at the areal scale, as well as the comfort distribution in landmark buffer zones at the point scale. This approach provides a more accurate study of urban visual comfort distribution, offering scientific evidence for urban planners and urban renewal practitioners. It helps them develop plans and renewal schemes that meet visual comfort requirements and enhance urban aesthetics. This not only improves the overall visual effect and comfort of the urban environment but also enhances residents' quality of life and the city's attractiveness, injecting new vitality into urban development.
  随着城市化进程的不断推进，高楼遮蔽了天空，自然的绿化越来越少，头顶的天空也越来越少，人们对于城市空间视觉舒适度的关注度越来越高，人们更希望在日常出行过程中能够享受更加舒适的景观和光照。近年来，深圳作为森林城市、花园城市典范，在城市的绿化建设中进行了不懈的努力。如何更好地通过大数据和新方法来研究城市视觉舒适度的分布，又应该如何根据这些分布来指导城市未来的规划和建设，已经成为城市规划的重心之一，城市空间的视觉舒适度已然成为作为提升居民生活质量和塑造城市形象的关键因素。
  在大数据时代，百度街景作为了解城市真实街景的重要渠道，已经成为城市大数据分析的主要来源。而在近期AI风潮的赋能下，以Unet为代表的一批优秀地物分割模型也已经成为街景地物分析的重要方式。通过不同点位的地物占比和问卷融合分析，可以综合性地研究现实世界中的街景地物是如何影响城市视觉舒适度。另外，机器学习时代的开启也为新的研究注入活力。神经网络、决策树等机器学习方法能够解决很多以往难以解决的问题，凭借着优秀的分类和集成方法，随机森林作为一种高效的模型能够较好地学习训练到各种类型的特征关系，并且能够根据新的特征求解出相应的预测结果。
  传统的城市视觉舒适度分析往往只关注景观的简单分析，而忽略日照采光对于城市视觉舒适度的影响。一些以cesium为代表的三维仿真平台开始在新一轮的视觉分析中崭露头角，它们能够真实模拟城市中的光影变化，详细展示城市的空间布局和建筑结构,为视觉舒适度分析提供了精确的空间数据，同时可以作为可视化的优秀方式融入相关的研究当中。
  本研究综合视觉舒适度中的日照采光和街景地物分割因素，采用随机森林模型在问卷调查中获取人们对于街景地物分布和日照累计采光的综合感评分，从而预测出全城市的舒适度分布，并进一步在街道上进行线尺度的空间插值，并在面尺度上进行全市分交通小区的分布规律探索，在点尺度上进行全市地标缓冲区的舒适度分布分析，更准确地研究城市视觉舒适度分布，为城市规划者和城市更新工作者提供科学的依据，帮助他们制定出既符合视觉舒适度要求，又能提升城市美感的规划和更新方案。这不仅能够改善城市环境的整体视觉效果和视觉舒适度，还能提升居民的生活质量和城市的吸引力，为城市发展注入新的活力。

II. Design Philosophy
二、设计思想

2.1 Design Concept
2.1. 设计思路

(See the attached file for the design concept diagram)
(设计思路图见附件文件)

2.2 Design Innovation
2.2. 设计创新

(1) Integration of daylighting in visual comfort analysis. Traditional urban visual comfort research methods are limited to general photo analysis. This work incorporates daylighting indicators and innovatively uses the Cesium 3D urban environment to simulate cumulative daylighting, making visual comfort more comprehensive and scientific.
（1）融合日照采光来对视觉舒适度进行分析。传统城市视觉舒适度研究方法局限于一般化的照片分析，本次作品融合日照采光指标，并创新地使用cesium城市三维环境模拟日照累计，使得视觉舒适度更加全面科学。

(2) In-depth application of machine learning methods in the model. Traditional urban visual comfort models rely on simple linear weighted models. This work uses questionnaire results to train a random forest model, achieving nonlinear fitting and prediction of urban visual comfort.
（2）机器学习方法在模型中的深度应用。传统城市视觉舒适度模型依赖于简单线性加权模型，本次作品利用问卷结果训练随机森林模型，实现对于城市视觉舒适度的非线性拟合和预测。

(3) Expanded analysis based on a multi-perspective approach. After obtaining the distribution of visual comfort, this study attempts to verify it at the areal scale of traffic zones and conducts visual comfort research in buffer zones around points of interest closely related to visual comfort, providing more targeted and comprehensive analysis.
（3）基于多元视角的拓展分析。在得到视觉舒适度的分布后，尝试以交通小区的面尺度进行印证，且在与视觉舒适度联系密切的风景名胜兴趣点进行缓冲区的视觉舒适度研究，进行了更有针对性、更全面的分析

III. Main Functions
三、主要功能

The main functions of this work include data processing for daylighting, data processing for street view analysis, data processing for questionnaire surveys, model training and application, and result analysis.
本次作品主要功能包括日照采光部分数据处理、街景分析部分数据处理、问卷调查部分数据处理、模型训练与应用、结果分析。

3.1 Data Processing for Daylighting
3.1 日照采光部分数据处理

A digital surface model is created by integrating terrain raster data and building data. The cumulative daylighting duration for the summer solstice is calculated for the entire city's digital surface model. The field of view buffer zones for all street points are solved, and the average value of the buffer zone raster for each street point is obtained, which serves as the cumulative daylighting indicator for that point.
使用地形栅格数据和建筑数据进行综合叠加得到数字表面模型，对于全市数字表面模型求解夏至日累计时长对应栅格，并求解所有街道点的视野缓冲区，依次得到所有街景点的缓冲区栅格平均值，作为该点的累计日照采光指标。

(1) Digital surface model solution. Input terrain raster data and building data to create a related model. The model process includes: converting building vector data to raster, masking the DEM range according to the building vector and performing zonal statistical mean values, applying a low-pass filter for overall Gaussian filtering, resampling to unify the two raster datasets, and using the raster calculator to overlay the raster data to obtain the digital surface model.
（1）数字表面模型求解。输入地形栅格数据和建筑数据，创建相关model，model的流程包括：建筑矢量数据面转栅格、按建筑矢量对应掩膜划出DEM范围并分区统计均值、使用低通滤波器进行整体高斯滤波处理、使用重采样统一两栅格数据、使用栅格计算器叠加栅格数据，最后可以得到数字表面模型。

(2) Solution for the raster corresponding to the cumulative duration of the summer solstice. Input the digital surface model and use a model to solve it. The model process involves: calculating the solar altitude and azimuth angles for each moment of the day in Shenzhen on the summer solstice, using the hillshade function to solve the light and shadow raster for the digital surface model at different times, and reclassifying each raster into binary values (0 and 1) representing shadow and light rasters. Subsequently, the raster calculator is used to sum all the rasters to obtain the total overlaid raster, which corresponds to the cumulative duration of the summer solstice.
（2）夏至日累计时长对应栅格求解。输入数字表面模型，同样使用model进行求解，model的流程有：计算出深圳市夏至日白天各时刻对应的太阳高度角和方位角，使用山体阴影功能对数字表面模型求解出不同时刻对应的光照阴影栅格，同时各自进行重分类处理，全部划分仅有0和1的栅格，代表阴影栅格和光照栅格。随后，使用栅格计算器对所有栅格进行累加，最后可以得到总的叠加栅格，即夏至日累计时长对应栅格。

(3) Solution for the cumulative daylighting indicator for points. Input street points, then calculate the 200m field of view buffer zone, and input the previously obtained overall daylighting distribution raster. Perform zonal statistical mean values for the 200m buffer zone of each point to obtain the daylighting indicator for that point.
（3）对于点的累计日照采光指标求解。输入街道点，随后求取视野200m缓冲区，再输入之前求得的日照累计总体分布栅格，针对每个点200m缓冲区分区统计均值，即可得到说有点的日照采光指标。

3.2 Data Processing for Street View Analysis
3.2 街景分析部分数据处理

Baidu Street View data is used to extract street view images with significant features and import them into ArcGIS Pro for semantic sample annotation and model training. The trained model is then used to perform semantic segmentation and recognition on street view photos to obtain spatial semantics for sky, buildings, roads, and green spaces, generating spatial visual description data.
使用百度街景数据，抽取具有显著特征的街景图片导入ArcGIS pro，标注语义样本，使用训练深度学习模型工具训练模型。利用训练后的模型对街景照片进行语义分割与识别，获取天空、建筑、道路、绿化四类空间语义，生成空间视觉描述数据。

(1) Street view image annotation. Among the total street view images, select a batch of images with significant features (large differences in landscape) and import them into the ArcGIS Pro environment. Using the ArcGIS Pro image classification tool, create a training sample manager for each street view image to be trained, and manually annotate each image using a four-category scheme to form a set of manually annotated vector data.
（1）街景图像标注。在总街景图片中，找到较为显著的一批街景照片（景观等差异较大），导入ArcGIS pro环境，使用ArcGIS pro影像分类工具，为每一张需训练的街景照片创建训练样本管理器，采用四分类方案，进行每一张街景的人工标注，形成人工标注矢量数据。

(2) Deep learning model training. Write a script to export training data for deep learning from ArcGIS Pro to process the manually annotated vector data into training dataset slices. Further use the deep learning model training function with the Unet neural network to train the corresponding deep learning model.
（2）深度学习模型训练。编写调用ArcGIS pro 导出训练数据以供深度学习的脚本处理人工标注矢量数据形成训练数据集分类切片，进一步使用训练深度学习模型功能，采用Unet神经网络训练出相应深度学习模型。

(3) Street object segmentation and recognition. Using the trained deep learning model, input all street view images to identify the spatial semantic distribution of the four elements in all images.
（3）街景地物分割与识别。利用训练后的深度学习模型，输入全部街景图像，识别出所有图像中四类要素的空间语义分布。

(4) Image spatial semantic statistics. Use the model builder function in ArcGIS Pro to create a model that integrates tools such as raster-to-vector conversion, adding geographic features, and statistical analysis of geographic features to quantify the area proportions of each category.
（4）图像空间语义统计。使用ArcGIS pro中的模型构建功能，创建模型，综合使用栅格转矢量、添加地理要素、统计地理要素等工具，量化计算各个类别的面积占比。

3.3 Data Processing for Questionnaire Surveys
3.3 问卷调查部分数据处理

(1) Questionnaire creation. Extract the coordinates of 20 feature-significant street view points, obtain the corresponding real street view photos, and use the Cesium simulation software to create short videos of the cumulative daylighting changes on the summer solstice for each point. The questionnaire is divided into 20 questions, where volunteers evaluate visual comfort based on real street view photos and corresponding daylighting videos.
（1）问卷制作。提取20个特征显著街景点位的坐标值，进而求出对应点位的真实街景照片，同时使用cesium仿真软件模拟出对应点位的夏至日日照累计变化短视频。在问卷中分成20道题目，志愿者们将通过真实街景照片和对应日照累计短视频进行视觉舒适度的评价。

(2) Questionnaire collection and data preprocessing. After approximately 100 volunteers complete the questionnaire, summarize the results and remove abnormal samples, such as incomplete questionnaires or those with all high or all low values. After processing, the questionnaire will form a neat scoring table for input into the subsequent model training.
（2）问卷搜集和数据预处理。在约100位志愿者进行问卷填写之后汇总问卷结果，对问卷结果中的异常样本进行剔除，比如问卷样本残缺的，或是全为高或者全为低的异常值。经过处理，问卷最后将形成一张规整的评分表，用于输入后续模型训练。

3.4 Model Training and Prediction
3.4模型训练与预测 

(1) Model training. The random forest model, as an excellent machine learning model, performs better than other models in small sample learning. Therefore, the visual comfort scores obtained from the questionnaire survey for all street view points are used as the dependent variable, and the corresponding daylighting and street view indicators are used as independent variable attributes to train the random forest model. This results in an urban visual comfort evaluation model and determines the importance of different indicators.
（1）模型训练。随机森林作为一种优秀的机器学习模型，在小样本学习上相对于其它模型更胜一筹，因此，这里将问卷调查得到的所有街景点对应视觉舒适度作为因变量，其对应的日照采光指标和街景指标作为自变量属性加入到随机森林模型中进行训练，得到城市视觉舒适度评价模型，并且求出不同指标的重要性占比。

(2) Model prediction. The trained model is applied to all street view points across the city to obtain the corresponding visual comfort scores. Spatial interpolation is then performed at the street linear scale to obtain the spatial distribution.
（2）模型预测。将训练出的模型对全市所有街景点进行应用预测，得到相应视觉舒适度，并且在街道线尺度进行空间插值，得到相应的空间内容。

(3) Urban spatial point interpolation. Use inverse distance weighting interpolation for each point's visual comfort score to obtain the overall visual comfort distribution in Nanshan District.
（3）城市空间点插值。面向每个点的视觉舒适度使用反距离权重插值，得到南山区视觉舒适度总体分布

IV. Result Analysis and Presentation
四、结果分析与成果展示

From the DSM elevation map of Nanshan District, we can observe the main topographical undulations and the distribution of buildings in the district. In the southern and northern parts of Nanshan, there are large areas of hills with few buildings. We can also see that the central part of Nanshan is mainly characterized by densely populated buildings, which appear as dense clusters of small black dots on the map, corresponding to high-rise building complexes, and the terrain is relatively flat.
After the complete processing of geographical data, we can obtain the visual comfort interpolation results for the entire area of Nanshan District in Shenzhen, which can be compared with the DSM elevation map of Nanshan District. The low values of visual comfort in the high-rise building areas of Nanshan District indicate that these densely built-up areas have a significant impact on visual comfort. In contrast, the northern part of Nanshan District, which features hilly terrain with greater topographical undulations, shows high values of visual comfort, suggesting that large green areas and hills can significantly enhance visual comfort. However, an interesting finding is that the visual comfort in the low-lying hilly areas of southern Nanshan does not show a significantly low value. Observing the densely built-up high-rise areas adjacent to these hills, we can infer that the visual comfort in the low-lying hilly areas is reduced due to the obstruction caused by the surrounding high-rise buildings. In the northern hilly areas, the higher elevation and fewer adjacent high-rise buildings mean that these areas are less affected by building obstructions.
In addition to the impact of building obstructions, there are also more diverse factors at play. Analysis of other local areas reveals that the visual comfort in the southeastern coastal region is generally higher. It can be inferred that the greening planning in coastal areas is more comprehensive compared to the urban clusters inland, and the better sky openness on the sea side makes the southeastern coastal region of Nanshan a local high-value area for visual comfort.
We can also compare the visual comfort distribution map of Nanshan District's transportation sub-areas with the overall visual comfort interpolation results. The zoning statistical patterns of the transportation sub-areas show certain similarities with the overall interpolation distribution patterns, further confirming that visual comfort is generally lower in the central areas of Nanshan and increases towards the edges, especially along the north-south axis.
Moreover, visual comfort from the perspective of scenic spots has always been a focus of attention. Therefore, by selecting the visual comfort distribution results in the buffer zones of scenic spot POIs in Nanshan District, we can see that most of the scenic spots in Nanshan are mainly distributed in the central, eastern, and northern parts of the district. In terms of visual comfort distribution, low values are mainly found in the central and northern parts near the south, and the same is true for the inland parts of the eastern region. However, the visual comfort in the scenic spots along the eastern coast is relatively good. The low values in the northern parts near the south can be inferred to be due to the proximity to the densely built-up high-rise area in the south, which exerts an influence on visual comfort, coupled with insufficient greening construction in these areas. In contrast, in the eastern coastal region, despite being adjacent to the high-rise building area, the greening construction is better. Although the buildings are densely packed, the appropriate layout of the high-rise buildings reduces the impact of building obstructions, resulting in better visual comfort.
我们从南山区DSM海拔示意图中，可以看出南山区的主要地形起伏状况和建筑分布情况，其中在南山南部和北部有着大片的丘陵，少建筑；我们还可以发现在南山中部地区主要是建筑分布密集点，可以在图上看到密密麻麻的黑色小点，对应高楼集群，地形平坦。
在经过完整的地理数据处理之后，我们可以得到深圳市南山区全域的视觉舒适度插值结果，这和南山区SDM海拔示意图形成了一定比对。在南山区的高楼密集区确实存在着视觉舒适度低值，这意味着高楼密集区对视觉舒适度产生了较大的影响，而在南山区北部的丘陵等地形起伏较大的区域，视觉舒适度也是产生了一个高值，也说明大块绿地和山地能够显著提高视觉舒适度。但是一个非常有意思的发现是，南山区南部低矮丘陵区的舒适度并没有呈现显著低值，可以观察到在紧邻丘陵的区域同样存在这密集的高楼区，因此可以推断是附近密集的高楼区的遮挡给低矮丘陵区带来了视觉舒适度的降低。而在北部丘陵区，由于海拔相对较高且邻接高楼数量较少，因此北部丘陵区较少收到高楼遮蔽的影响。
除了高楼遮蔽的影响之外，实际上也有着更多元因素的影响。通过其他局部地区的分析，可以发现在东南沿海地区，视觉舒适度普遍较高，可以推断在临海地区绿化规划相对于内部城市集群来说更加完善，而且靠海一侧有着较好的天空开阔度，使得南山东南沿海地区成为舒适度的局部高值区域。
我们同样可以比对南山区交通小区视觉舒适度分布图和南山区视觉舒适度插值结果，交通小区的分区统计规律和总体插值分布规律有着一定的相似性，进一步印证了在南山内部地区，舒适度普遍较低，而越向边缘靠近，舒适度越高，尤其在南北轴线上表现显著。
此外，视觉舒适度在风景名胜视角一直受人们关注，因此，选取南山区风景名胜POI缓冲区研究其视觉舒适度分布结果，可以发现，南山区的大部分风景名胜区主要分布在内部地区、东部地区和北部地区。从视觉舒适度分布来看，内部地区和北部地区近南处主要呈现低值分布，在东部地区内陆部分也是如此，而在东部沿海地区风景名胜区的视觉舒适度都较好，北部地区近南处低值分布的原因可以推断为虽然位于南山北部地区，但是距离南部高楼密集带太近，因此也收到高楼的影响，但是自身绿化建设也有所欠缺，而在东部沿海地区，城市虽然邻近高楼密集带，但是绿化建设较好，高楼虽然密集，但是高楼采用更恰当的布局减小高楼遮蔽的影响，因此舒适度较好。

V. Summary and Outlook
五、总结和展望

The guiding principle of this study is people-oriented, considering the impact of daylighting and street view on urban visual comfort with more comprehensive indicators. By using machine learning models represented by Random Forest for training and prediction, the precision of urban visual comfort calculation is achieved. During the analysis, from the Unet neural network segmentation tool to the raster calculation tool, this study employs a variety of ArcGIS Pro tools to uncover hidden spatial information in maps, demonstrating the geographical design team's proficiency in geographical design and research.
Visual comfort, as an important factor in urban planning and urban renewal, is increasingly valued by scholars in various fields. In our study, we comprehensively analyze visual comfort with more comprehensive indicators and conduct targeted analysis of regional visual comfort distribution patterns, dominant factors, and improvement strategies through zoning statistics and point buffer zone analysis. According to the results, continuing to optimize greening construction and improve building layout in high-rise building areas will be an important measure to improve urban visual comfort in the future. In our research, the indicators still have limitations, and the analysis methods have room for improvement. We hope that future research can more comprehensively analyze urban visual comfort.
以人为本是本研究的指导思想，以更全面的指标，综合考虑日照采光和街景视野对于城市视觉舒适度的影响，并以随机森林为代表的机器学习模型进行训练和预测，实现了城市视觉舒适度的求解精确性。在分析的过程中，从Unet神经网络分割工具到栅格计算工具，本研究运用了多样的ArcGIS pro工具，挖掘地图中隐藏的空间信息，体现了地理设计团队对于地理设计和研究的掌握程度。
视觉舒适度作为城市规划、城市更新中的重要影响因素，在当今社会中越来越受到各界学者的重视，在我们的研究中，我们以更全面的指标解析视觉舒适度，并以分区统计和点缓冲区分析的形式针对性分析地区视觉舒适度分布规律、主导因素和改进策略，根据结果来看，在高楼密集区继续优化绿化建设，完善房屋格局构建将成为未来改善城市视觉舒适度的重要举措。在我们的研究中，指标仍然具有局限性，分析方法也有升级的空间，希望未来有更先进的研究能够更全面地解析城市视觉舒适度。




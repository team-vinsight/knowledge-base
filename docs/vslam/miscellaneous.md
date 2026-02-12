# Miscellaneous

## Relevant Papers & Links

*   **SELM-SLAM3**: [Deep Learning-Powered Visual SLAM Aimed at Assisting Visually Impaired Navigation](https://www.scitepress.org/Papers/2025/133382/133382.pdf) - [GitHub](https://github.com/banafshebamdad/SELM-SLAM3)
    *   **Key Tech**: SuperPoint (Feature Extraction), LightGlue (Matcher), ONNX Runtime (C++).
    *   **Innovation**: An RGB-D SLAM framework extending ORB-SLAM3 by replacing ORB features/matching with deep learning alternatives (SuperPoint/LightGlue). It features a fully C++ inference pipeline using ONNX Runtime, removing Python dependencies, and introduces a new matching strategy for deep features to assist visually impaired navigation.

*   **SuperPoint-SLAM3**: [Augmenting ORB-SLAM3 with Deep Features](https://arxiv.org/pdf/2506.13089)
    *   **Key Tech**: SuperPoint (Self-supervised detector-descriptor), Adaptive Non-Maximal Suppression (ANMS), NetVLAD (Loop Closure).
    *   **Innovation**: A drop-in upgrade for ORB-SLAM3 that replaces ORB with SuperPoint and enforces spatially uniform keypoints using ANMS. It also integrates a lightweight NetVLAD place-recognition head for learning-based loop closure, significantly reducing translation and rotation errors on datasets like KITTI and EuRoC.

*   **Photometric SLAM**: [SLAM with Mapping Based on Photometric Information and ORB Features](https://journal.ecust.edu.cn/en/article/id/a8fb466c-cee8-4f9d-a124-7af1aa7eca39)
    *   **Key Tech**: Photometric error minimization (Direct Method), ORB Features.
    *   **Innovation**: A hybrid approach that combines direct methods (using photometric information) with feature-based ORB-SLAM. This fusion aims to improve mapping and tracking robustness, particularly in environments where traditional feature extraction might struggle (e.g., low texture).

*   **Deep-UAV SLAM**: [SuperPoint and SuperGlue enhanced SLAM](https://isprs-archives.copernicus.org/articles/XLVIII-1-W5-2025/177/2025/index.html)
    *   **Key Tech**: SuperPoint (Extraction), SuperGlue (Matching).
    *   **Innovation**: Specifically targets UAV aerial navigation by upgrading the front-end of ORB-SLAM3 with deep learning features and matchers. It demonstrates higher robustness and accuracy in dynamic outdoor aerial scenarios compared to classical handcrafted features.

*   **Light-SLAM**: [Light-SLAM: A Robust Deep-Learning Visual SLAM System Based on LightGlue under Challenging Lighting Conditions](https://arxiv.org/pdf/2407.02382)
    *   **Key Tech**: LightGlue (Matching), Deep local feature descriptors.
    *   **Innovation**: A robust hybrid visual SLAM system (supporting Mono/Stereo/RGB-D) built around the LightGlue network. It is designed to handle challenging lighting conditions (low-light, strong variations) more effectively than traditional or other deep methods, while maintaining real-time performance on GPUs.

*   **PCR-ORB**: [PCR-ORB: Enhanced ORB-SLAM3 with Point Cloud Refinement Using Deep Learning-Based Dynamic Object Filtering](https://www.researchgate.net/publication/399176409_PCR-ORB_Enhanced_ORB-SLAM3_with_Point_Cloud_Refinement_Using_Deep_Learning-Based_Dynamic_Object_Filtering)
    *   **Key Tech**: YOLOv8 (Semantic Segmentation), Point Cloud Refinement, CUDA acceleration.
    *   **Innovation**: enhancing ORB-SLAM3 for dynamic environments by integrating YOLOv8 for dynamic object filtering and a multi-stage point cloud refinement process (ground estimation, sky removal, edge filtering). It utilizes CUDA to ensure real-time performance.

*   **SuperGlue**: [SuperGlue: Learning Feature Matching with Graph Neural Networks](https://arxiv.org/pdf/1911.11763) - [GitHub](https://github.com/magicleap/SuperGluePretrainedNetwork)
    *   **Key Tech**: Graph Neural Networks (GNN), Optimal Transport, Attention Mechanisms.
    *   **Innovation**: A neural network that matches two sets of local features by jointly finding correspondences and rejecting non-matchable points. It learns priors over geometric transformations and regularities of the 3D world, replacing traditional hand-designed matching heuristics.

*   **LightGlue**: [LightGlue: Local Feature Matching at Light Speed](https://arxiv.org/pdf/2306.13643) - [GitHub](https://github.com/cvg/LightGlue)
    *   **Key Tech**: Adaptive Deep Neural Network, Transformer-based architecture.
    *   **Innovation**: A lightweight and efficient evolution of SuperGlue. It is adaptive to the difficulty of the matching problem (faster inference on easy pairs), easier to train, and more memory/compute efficient, making it ideal for latency-sensitive applications like SLAM.

*   **SuperPoint**: [SuperPoint: Self-Supervised Interest Point Detection and Description](https://arxiv.org/pdf/1712.07629) - [GitHub](https://github.com/magicleap/SuperPointPretrainedNetwork)
    *   **Key Tech**: Fully-convolutional neural network, Homographic Adaptation, Self-supervised learning.
    *   **Innovation**: A self-supervised framework for training interest point detectors and descriptors that operates on full-sized images in a single forward pass. It introduces "Homographic Adaptation" to boost repeatability and enable cross-domain adaptation (learning from synthetic data to apply to real-world images).

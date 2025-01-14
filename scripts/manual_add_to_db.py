"""
This file uploads 2 things: 
- workflows 
- recipes

Workflows go into "workflows-data"
Recipes go into "workflows-recipes"
"""
import os
from relevanceai import Client

client = Client(token=os.getenv("SUPPORT_ACTIVATION_TOKEN"), force_refresh=True)

ds = client.Dataset("workflows-recipes")

COLAB_PREFIX = "https://colab.research.google.com/github/RelevanceAI/workflows/blob/main/"
WORKFLOWS = [
        {
            "_id" : "bias-detection",
            "type": "workflow",
            "title": "Bias Detection",
            "description": "Detect bias in your vectorizers",
            "colab_link": COLAB_PREFIX + "workflows/bias-detection/✨Vector_Based_Bias_Detection_With_Relevance_AI.ipynb",
            "use_cases": ["Gender bias", "Category bias", "Unsupervised bias detection"],
            "documentation_links": [{"title": "SDK Reference", "url": "https://relevanceai.readthedocs.io/en/development/relevanceai.bias_detection.html"}],
            "video_links": [],
            "new": True,
            "prerequisites": ["List of bias categories", "List of data items (images/text) to vectorize", "Vectorizer"],
        },
        {
            "_id" : "cluster-reports",
            "colab_link": COLAB_PREFIX + "workflows/cluster-reporting/%F0%9F%91%8D_Cluster_Reports_With_Relevance_AI.ipynb",
            "type": "workflow",
            "title": "Cluster Evaluation Report",
            "description": "Automatically analyse your clusters using a variety of metrics to improve cluster performance",
            "prerequisites": ["A dataset with vectors and clusters OR", "An X array with cluster labels and clustering model"],
            "use_cases": ["Ensuring proper topics are extracted", "Ensuring customers are properly segmented"],
            "documentation_links": [{"title": "SDK Reference", "url": "https://relevanceai.readthedocs.io/en/development/relevanceai.cluster_report.html#"}],
            "video_links": [],
            "new": True
        },
        {
            "_id" : "subclustering",
            "type": "workflow",
            "colab_link": COLAB_PREFIX + "workflows/subclustering/basic_subclustering.ipynb",
            "title": "Subclustering",
            "description": "Clustering within clusters",
            "prerequisites": ["A dataset with vectors and clusters"],
            "use_cases": ["Infinitely drilling down into your clusters to see what they comprise of"],
            "documentation_links": [{"title": "SDK Reference", "url": "https://relevanceai.readthedocs.io/en/development/subclustering.html"}],
            "video_links": [],
            "new": True
        },
        {
            "_id": "keyphrases",
            "type": "workflow",
            "colab_link": COLAB_PREFIX + "workflows/keyphrases/KeyPhrases_Workflow.ipynb",
            "title": "Keyphrases",
            "description": "Identify the most common keyphrases in a text field and clusters and see how we enable infinite hacking to finetune your keyphrases.",
            "prerequisites": ["Text fields", "(Optional) Cluster fields"],
            "use_cases": ["Automated keyphrase detection in clusters"],
            "documentation_links": [{"SDK Reference": "https://relevanceai.readthedocs.io/en/latest/dataset.html#relevanceai.dataset_api.dataset_operations.Operations.keyphrases"}],
            "video_links": [],
            "new": True
        },
        {
            "_id" : "vector-rake",
            "title": "Vector-Rake Keyphrases",
            "description": "Keyphrase extraction using a nearest-neighbor algorithm on top of the normal RAKE algorithm",
            "colab_link": COLAB_PREFIX + "workflows/vector-rake/vector_rake.ipynb",
            "use_cases": ["auto-labeling documents"],
            "documentation_links": [],
            "video_links": [],
            "new": True,
            "prerequisites": ["dataset with text field", "vectorized text field", "vectorizer"],
        },
        {
            "_id": "video-search",
            "type": "workflow",
            "colab_link": COLAB_PREFIX + "workflows/keyphrases/KeyPhrases_Workflow.ipynb",
            "title": "Video Search",
            "description": "Search videos using text to find the right frame you want.",
            "prerequisites": ["Mp4 video"],
            "use_cases": ["Video Search"],
            "documentation_links": [{"SDK Reference": "https://relevanceai.readthedocs.io/en/latest/dataset.html#relevanceai.dataset_api.dataset_operations.Operations.keyphrases"}],
            "video_links": [],
            "new": True,
            "coming_soon": True
        },
        {
            "_id": "video-clusters",
            "type": "workflow",
            "colab_link": COLAB_PREFIX + "workflows/keyphrases/KeyPhrases_Workflow.ipynb",
            "title": "Video Clustering",
            "description": "Get clusters to determine key different scenes in your video.",
#             "prerequisites": ["Mp4 video"],
#             "use_cases": ["Video Search"],
#             "documentation_links": [{"SDK Reference": "https://relevanceai.readthedocs.io/en/latest/dataset.html#relevanceai.dataset_api.dataset_operations.Operations.keyphrases"}],
#             "video_links": [],
#             "new": True,
            "coming_soon": True
        },
        {
            "_id": "impact-analysis",
            "type": "workflow",
            "colab_link": COLAB_PREFIX + "workflows/impact-analysis/impact-analysis.ipynb",
            "title": "Feature/Impact Analysis",
            "description": "Analyse the impact of your features and directly assess how important they are and their local/global impact on the KPI or metric.",
            "prerequisites": ["Dataset with encoded vectors and a variable to measure importance."],
            "use_cases": ["KPI Measurement", "Impact analysis"],
            "documentation_links": [],
            "video_links": [],
            "new": True,
            "coming_soon": False
        },
         {
            "_id": "pdf-ingestion",
            "type": "workflow",
            "colab_link": None,
            "title": "Insert PDFs",
            "description": "Insert highly unstructured PDFs in order to search images, flowcharts and build other vector applications/insights.",
#             "prerequisites": ["Mp4 video"],
#             "use_cases": ["Video Search"],
#             "documentation_links": [{"SDK Reference": "https://relevanceai.readthedocs.io/en/latest/dataset.html#relevanceai.dataset_api.dataset_operations.Operations.keyphrases"}],
#             "video_links": [],
            "new": True,
            "coming_soon": True
        },
        {
            "_id": "most-common-words-in-clusters",
            "type": "workflow",
            "colab_link": COLAB_PREFIX + "workflows/most-common-words-in-clusters/most-common-words-in-clusters.ipynb",
            "title": "Most Frequent Phrases In Clusters",
            "description": "Update your cluster explorer with the most frequently occurring word labels!",
            "prerequisites": ["Text fields", "Cluster fields", "Existing Deployable"],
            "use_cases": ["Automated Cluster Labelling"],
            "documentation_links": [{"SDK Reference": "https://relevanceai.readthedocs.io/en/development/dataset.html#relevanceai.dataset_api.dataset_operations.Operations.cluster_keyphrases"}],
            "video_links": [],
            "new": True,
            "coming_soon": False
        },
        {
            "_id": "community-detection",
            "type": "workflow",
            "colab_link": COLAB_PREFIX + "workflows/community-detection/Community_Detection_with_Relevance_AI.ipynb",
            "title": "Community Detection",
            "description": "Detect communities, or clusters, among embedding-transformed text fields or vectors.",
            "prerequisites": ["Text fields", "(Optional) Cluster fields"],
            "use_cases": ["Community detection of text fields and vectors"],
            "documentation_links": [{"SDK Reference": "https://relevanceai.readthedocs.io/en/latest/dataset.html?highlight=community#relevanceai.dataset_api.dataset_operations.Operations.community_detection"}],
            "video_links": [],
            "new": True
        },
        {
            "_id": "dimensionality-reduction",
            "type": "workflow",
            "colab_link": COLAB_PREFIX + "workflows/dr/Reduce_the_Dimensions_of_Your_Data_with_Relevance_AI.ipynb",
            "title": "Dimensionality Reduction",
            "description": "Reduce vector fields in your dataset down to fewer dimensions for easier visualisation (e.g. our 3D projector)",
            "prerequisites": [],
            "use_cases": [],
            "documentation_links": [{"SDK Reference": "https://relevanceai.readthedocs.io/en/latest/auto_reduce_dimensions.html"}],
            "video_links": [{"dr-workflows": "https://files.relevance.ai/v/2kFOGHU2jN6sKOx4NGl4"}],
            "new": False,
            "core": True,
        },
        {
            "_id": "media-upload",
            "type": "workflow",
            "colab_link": COLAB_PREFIX + "workflows/media_upload/💡_Upload_Audio_Images_Videos_Flow.ipynb",
            "title": "Media Upload",
            "description": "Learn how to upload images/videos/audio files to Relevance AI!",
            "prerequisites": ["Images or other media files to upload. These can be local or hosted online somewhere else already."],
            "use_cases": [],
            "documentation_links": [{"SDK Reference": "https://relevanceai.readthedocs.io/en/latest"}],
            "video_links": [],
            "new": True,
            "core": False,
        },
        
############### RECIPES

        {
            "_id": "dummy-datasets",
            "type": "dummy-dataset",
            "colab_link": COLAB_PREFIX + "workflows/dummy-datasets/Dummy_Datasets_Workflow.ipynb",
            "title": "Insert A Dummy Dataset",
            "description": "Insert a dummy dataset with this workflow.",
            "prerequisites": [],
            "use_cases": [],
            "documentation_links": [{"SDK Reference": "https://relevanceai.readthedocs.io/en/latest/available_datasets.html#relevanceai.datasets.get_dummy_ecommerce_dataset"}],
            "video_links": [],
            "new": True,
            "core": False,
        },
        {
            "_id": "pdf-search",
            "type": "recipe",
            "colab_link": None,
            "title": "PDF Search",
            "description": "Be able to search through all text and images in PDFs.",
            "prerequisites": ["PDFs"],
            "use_cases": ["PDF Search", "Flowchart Search"],
            "documentation_links": [{"SDK Reference": "https://relevanceai.readthedocs.io/en/latest/dataset.html#relevanceai.dataset_api.dataset_operations.Operations.vector_search"}],
            "video_links": [],
#             "new": True,
            "coming": True
        },
        {
            "_id": "figma-search",
            "type": "recipe",
            "colab_link": None,
            "title": "Figma Illustration Search",
            "description": "Upload all figma images and instantly be able to search them.",
            "prerequisites": ["Figma account"],
            "use_cases": ["Image Search", "Illustration search", "Designer Showcase"],
            "documentation_links": [{"SDK Reference": "https://relevanceai.readthedocs.io/en/latest/dataset.html#relevanceai.dataset_api.dataset_operations.Operations.vector_search"}],
            "video_links": [],
#             "new": True,
            "coming": True
        },
        {
            "_id": "figma-clusters",
            "type": "recipe",
            "colab_link": None,
            "title": "Figma Illustration Clusters",
            "description": "Group your illustrations to promote natural discovery of your illustrations.",
            "prerequisites": ["Figma account"],
            "use_cases": ["Illustration Search", "Designer Discovery", "Drawing Discovery"],
            "documentation_links": [],
            "video_links": [],
#             "new": True,
            "coming": True
        },
        {
            "_id": "crunchbase-clusters",
            "type": "recipe",
            "colab_link": None,
            "title": "Crunchbase Cluster Analysis",
            "description": "Group companies to discover similar properties between your companies.",
            "prerequisites": ["Crunchbase account"],
            "use_cases": ["Competitor Analysis", "Crunchbase"],
            "documentation_links": [],
            "video_links": [],
#             "new": True,
            "coming": True
        },
        {
            "_id": "twitter-analysis",
            "type": "recipe",
            "colab_link": COLAB_PREFIX + "workflows/twitter-analysis/AI_Twitter_Analysis_by_Relevance_AI.ipynb",
            "title": "Twitter Analysis",
            "description": "Analyse your tweets and view which images and tweets are the most/least popular!",
            "prerequisites": ["No requirements."], # not needed in future
            "use_cases": ["Analysing which tweets are the most popular."], # not needed in future
            "documentation_links": [], # not needed in future
            "video_links": [], # not needed in future
            "new": True,
            "recipe": True, # Required for recipes
            "feature_image_url": "https://relevance.ai/wp-content/uploads/2022/03/image-6.png",
            "blog_link": "https://relevance.ai/twitter-data-workflow-how-to-run-twitter-account-data-analysis/",
            "recipe_url": "https://relevance.ai",
            "logo_url": "https://www.svgrepo.com/show/22159/twitter.svg",
        },
    ]

results = ds.upsert_documents(WORKFLOWS)
print(results)


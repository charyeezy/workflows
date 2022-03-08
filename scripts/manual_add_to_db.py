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

# Workflows data
ds = client.Dataset("workflows-data")
ds.delete()

# Recipes data
recipes_ds = client.Dataset("workflows-recipes")

COLAB_PREFIX = "https://colab.research.google.com/github/RelevanceAI/workflows/blob/main/"
WORKFLOWS = [
        {
            "_id" : "bias-detection",
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
            "_id": "twitter-analysis",
            "colab_link": COLAB_PREFIX + "workflows/twitter-analysis/AI_Twitter_Analysis_by_Relevance_AI.ipynb",
            "title": "Twitter Analysis",
            "description": "Analyse your tweets and view which images and tweets are the most/least popular!",
            "prerequisites": ["No requirements."], # not needed in future
            "use_cases": ["Analysing which tweets are the most popular."], # not needed in future
            "documentation_links": [], # not needed in future
            "video_links": [], # not needed in future
            "new": True,
            "recipe": True, # Required for recipes
            "recipe_url": "https://relevance.ai"
        },
        {
            "_id": "keyphrases",
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
            "colab_link": None,
            "title": "Impact Analysis",
            "description": "Analyse the impact of your labels and features on direct KPIs.",
#             "prerequisites": ["Mp4 video"],
#             "use_cases": ["Video Search"],
#             "documentation_links": [{"SDK Reference": "https://relevanceai.readthedocs.io/en/latest/dataset.html#relevanceai.dataset_api.dataset_operations.Operations.keyphrases"}],
#             "video_links": [],
            "new": True,
            "coming_soon": True
        },
        {
            "_id": "community-detection",
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
        
#         {
#             "_id": "figma-search",
#             "colab_link": None,
#             "title": "Figma Illustration Search",
#             "description": "Upload all figma images and instantly be able to search them.",
#             "prerequisites": ["Figma account"],
#             "use_cases": ["Image Search", "Illustration search", "Designer Showcase"],
#             "documentation_links": [{"SDK Reference": "https://relevanceai.readthedocs.io/en/latest/dataset.html#relevanceai.dataset_api.dataset_operations.Operations.vector_search"}],
#             "video_links": [],
# #             "new": True,
#             "coming_soon": True
#         },
#         {
#             "_id": "figma-clusters",
#             "colab_link": None,
#             "title": "Figma Illustration Clusters",
#             "description": "Group your illustrations to promote natural discovery of your illustrations.",
#             "prerequisites": ["Figma account"],
#             "use_cases": ["Illustration Search", "Designer Discovery", "Drawing Discovery"],
#             "documentation_links": [],
#             "video_links": [],
# #             "new": True,
#             "coming_soon": True
#         },
#         {
#             "_id": "crunchbase-clusters",
#             "colab_link": None,
#             "title": "Crunchbase Cluster Analysis",
#             "description": "Group companies to discover similar properties between your companies.",
#             "prerequisites": ["Crunchbase account"],
#             "use_cases": ["Competitor Analysis", "Crunchbase"],
#             "documentation_links": [],
#             "video_links": [],
# #             "new": True,
#             "coming_soon": True
#         }
    ]


results = ds.upsert_documents(WORKFLOWS)
print(results)
RECIPES_DOCS = [
        {
            "_id": "twitter-analysis",
            "colab_link": COLAB_PREFIX + "workflows/twitter-analysis/AI_Twitter_Analysis_by_Relevance_AI.ipynb",
            "title": "Twitter Analysis",
            "description": "Analyse your tweets and view which images and tweets are the most/least popular!",
            "prerequisites": ["No requirements."],
            "use_cases": ["Analysing which tweets are the most popular."],
            "documentation_links": [],
            "video_links": [],
            "new": True
        },
        {
            "_id": "figma-search",
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
            "colab_link": None,
            "title": "Crunchbase Cluster Analysis",
            "description": "Group companies to discover similar properties between your companies.",
            "prerequisites": ["Crunchbase account"],
            "use_cases": ["Competitor Analysis", "Crunchbase"],
            "documentation_links": [],
            "video_links": [],
#             "new": True,
            "coming": True
        }
    ]

results = recipes_ds.upsert_documents(RECIPES_DOCS)
print(results)
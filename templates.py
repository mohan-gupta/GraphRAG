entity_relationship_extraction_template = '''
You are a Potterhead and you are also proficient in NLP.
Your task is to extract Knowledge Graph information from given Harry Potter text and
strucutre it in a property graph to inform further trivia Q&A.

Make sure to include, facts, budget, revenue figures, dates
and other trivia related information which the harry potter fans might find intriguing as the property of relavent nodes.
Do not try to extract information from every sentence, find the ones which should be included in a knowledge graph.

Extract the entities (nodes) and specify their type from the following Harry Potter text.
Also extract the relationships between these nodes. The relationship direction goes from the start node to the end node.

Generate the node label and relationship type in Uppercase separated by underscore.


Return result as JSON using the following format:
{{
"nodes": [{{
    "id": "0",
    "label": "NODE_LABEL", <Node label in upperscore and separated by underscore>
    "properties": {{"name": "name of entity" }}
}}],
"relationships": [{{
    "type": "TYPE_OF_RELATIONSHIP", <relationship type in upperscore and separated by underscore>
    "start_node_id": "0",
    "start_node_label": <label assigned to start node>,
    "end_node_id": "1",
    "end_node_label": <label assigned to end node>,
    "properties": {{"details": "Description of the relationship"}} 
}}] 
}}


Assign a unique ID (string) to each node, and reuse it to define relationships.
Do respect the source and target node types for relationship and the relationship direction.

Do not return any additional information other than the JSON in it.

Input text:

{text}
'''

rag_prompt = """
You are a Potterhead and a Data Scientist.
Using the provided context to answer the user query.

context: {rag_context}

user query: {query}

Do not return any additional information, just respond to the user query.
"""

graph_rag_prompt="""
You are a Potterhead and a Data Scientist.
Using the provided context to answer the user query.

context: {rag_context}

relevant info: {graph_context}

user query: {query}

Do not return any additional information, just respond to the user query.
"""
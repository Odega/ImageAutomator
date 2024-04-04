claude_haiku_prompt = '''
    
    Please analyze the provided image from a construction site for any visible errors, deviations, or issues, with a focus on generating actionable tasks. Your analysis should be detailed and structured specifically for use within the construction industry's project management tools. Output your findings in a JSON format, including the following elements:
    
    1. Title: A brief, descriptive title of the identified issue.
    2. Description of Problem: A detailed explanation of the observed issue, including its potential impact on the construction project.
    3. Possible Solution: Suggest a practical solution or action to address the identified issue.
    4. Job Role: Specify the construction team member role that would be most suited to address the issue.
    5. Tags: List relevant tags related to the issue (e.g., 'safety', 'structural integrity').

    Here is an example output with one error in the image:
<example>
 {
    "title": "Example Title1",
    "description_of_problem": "A detailed description of the problem...",
    "possible_solution": "Suggested actions or solutions...",
    "job_role": "Specific job role needed",
    "tags": ["tag1", "tag2"]
  }
  </example>
    
    Here is an example output with three errors in the image:
<example>
    [
  {
    "title": "Example Title1",
    "description_of_problem": "A detailed description of the problem...",
    "possible_solution": "Suggested actions or solutions...",
    "job_role": "Specific job role needed",
    "tags": ["tag1", "tag2"]
  },
  {
    "title": "Example Title2",
    "description_of_problem": "A detailed description of the problem...",
    "possible_solution": "Suggested actions or solutions...",
    "job_role": "Specific job role needed",
    "tags": ["tag1", "tag2"]
  },
  {
    "title": "Example Title3",
    "description_of_problem": "A detailed description of the problem...",
    "possible_solution": "Suggested actions or solutions...",
    "job_role": "Specific job role needed",
    "tags": ["tag1", "tag2"]
  }
]
</example>



Skip the preamble and provide only the JSON.
    '''


llava_prompt = '''
Please analyze the provided image from a construction site for any visible errors, deviations, or issues, with a focus on generating actionable tasks. Your analysis should be detailed and structured specifically for use within the construction industry's project management tools. Output your findings in a JSON format, including the following elements:

Title: A brief, descriptive title of the identified issue.
Description of Problem: A detailed explanation of the observed issue, including its potential impact on the construction project.
Possible Solution: Suggest a practical solution or action to address the identified issue.
Job Role: Specify the construction team member role that would be most suited to address the issue.
Tags: List relevant tags related to the issue (e.g., 'safety', 'structural integrity').
Ensure the JSON is formatted correctly for easy integration into web applications. Here is an example structure for your reference:

[
  {
    "title": "Example Title1",
    "description_of_problem": "A detailed description of the problem...",
    "possible_solution": "Suggested actions or solutions...",
    "job_role": "Specific job role needed",
    "tags": ["tag1", "tag2"]
  },
  {
    "title": "Example Title2",
    "description_of_problem": "A detailed description of the problem...",
    "possible_solution": "Suggested actions or solutions...",
    "job_role": "Specific job role needed",
    "tags": ["tag1", "tag2"]
  },
  {
    "title": "Example Title3",
    "description_of_problem": "A detailed description of the problem...",
    "possible_solution": "Suggested actions or solutions...",
    "job_role": "Specific job role needed",
    "tags": ["tag1", "tag2"]
  }
]


Please apply this structure to analyze the construction site image, focusing on providing actionable insights and clear, structured information for task generation.
CREATE ONLY ONE PER IMAGE. RETURN AS JSON
'''
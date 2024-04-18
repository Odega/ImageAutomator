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

hackathon_prompt = '''
    
    Analyze the provided images and output in json format. IMPORTANT THAT YOU KEEP THE STRUCTURE POVIDED IN THE EXAMPLES.
    Also we also want to provide what type of document is being analyzed: Receipt, invoice, etc. as Document_type

    Here is an example output.
<example>
 {
 "Document_type": "Receipt",
  "Total": "$69.00",
  "Transaction ID": "55G91941UV310752C",
  "Transaction date": "Feb 17, 2022 03:46:40 PST",
  "Merchant name": "AppSumo",
  "Merchant email": "support@appsumo.com",
  "Invoice ID": "98744a56-bbb9-4d65-abde-58f450e4c12f",
  "Products List": [
    {
      "Product name": "Parsio.io",
      "Unit price": "$69.00",
      "Qty": "1",
      "Amount": "$69.00 USD"
    }
  ]
}
  </example>
Another example:
<example>
{
    "Document_type": "CustomerInvoice",
    "CustomerName ": "Sirius Greenland ApS",
    "InvoiceAddress": "Ittukasiup AQQ.",
    "InvoiceZipcode": "3911 Sisimiut",
    "InvoiceCountry": "Greenland",
    "DeliveryName": "AQQALUK ABESLEN",
    "DeliveryAddress":"QAQORTOQ AUTO OG MARINE APS",
    "DeliveryZipcode": "3920 QAQORTOQ",
    "DeliveryCountry": "Greenland",
    "InvoiceNumber": "128105",
    "OrderNumber": "448162",
    "Account": "299863700",
    "InvoiceDate": "29-02-2024",
    "OrganizationNumber": "39631784",
    "YourReference": "qaqortoq",
    "NetAmount": "77097,03",
    "TotalAmount": "77097,03",
    "PaymentTerms":"Lbmd 25 dage",
    "DueDate": "25-03-2024",
    "PaymentReference": "+71<000000001281054+84403792>",
    "BankAccount": "8090 539802",
    "OrderLines": [
        {
            "ArticleNumber": "21924266",
            "ArticleName": "PROPELLER KIT",
            "Quantity": "1",
            "Unit": "STK",
            "Discount": "25,0%",
            "UnitPrice": "6703,00",
            "Price": "5027,25"
        },
        {
            "ArticleNumber": "3868727",
            "ArticleName": "Automatic Drive",
            "Quantity": "1",
            "Unit": "STK",
            "Discount": "22,0%",
            "UnitPrice": "88451,00",
            "Price": "68991,78"
        },
        {
            "ArticleNumber": "FR",
            "ArticleName": "FRAGT VIA SKIB",
            "Quantity": "1",
            "Unit": "STK",
            "Discount": "",
            "UnitPrice": "3078,00",
            "Price": "3078,00"
        }
    ],
    "Attachments": [
        {
            "DocumentType": "SupplierInvoice",
            "InvoiceNumber": "128105",
            "SupplierName": "JL Marine - J L Skibsservice - Volvo",
            "SupplierAddress": "Sildevej 16",
            "SupplierZipcode": "9970 Strandby",
            "SupplierCountry": "Danmark",
            "SupplierNumber": "911202012",
            "LedgerDate": "14.03.24",
            "OrderLines": [
                {
                    "ArticleNumber": "V_21924266",
                    "ArticleName": "PROPELLER KIT",
                    "Quantity": "1",
                    "Unit": "STK",
                    "Discount": "25,0%",
                    "UnitPrice": "6703,00",
                    "Price": "5027,25"
                },
                {
                    "ArticleNumber": "V_3868727",
                    "ArticleName": "Drive",
                    "Quantity": "1",
                    "Unit": "STK",
                    "Discount": "22,0%",
                    "UnitPrice": "88451,00",
                    "Price": "68991,78"
                }
            ]
        }
    ]
}
</example>
  

Look for words such as "Receipt", "Invoice" etc to be able to determine the type of document being analyzed, and use it in Document_type.

Skip the preamble and provide only the JSON. <important> IT IS VERY IMPORTANT THAT YOU Translate the information to ENGLISH </important
    '''
# Deploy the Azure AI Studio Starter template 

The "Azure AI Studio Starter" template is recommended for users looking to get started with Azure AI Studio.

Resources Included:
- AI Hub with dependent resources
- AI project
- AI Services
- An online endpoint

## Prerequisites

Requires [Azure Developer CLI](https://learn.microsoft.com/de-de/azure/developer/azure-developer-cli/overview?tabs=linux) installation:

```bash
winget add Microsoft.Azd
```

## Initialize & Deployment

Initialize the Azure AI Studio Starter template:

```bash
azd init --template https://github.com/Azure-Samples/azd-aistudio-starter
```

>Note: Additional templates would be `azd init --template Azure-Samples/azure-search-openai-demo` or `azd init --template Azure-Samples/azure-enterprise-rag`

```bash
azd up
```
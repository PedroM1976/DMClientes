# Dashboard de clientes — listas importadas independentes

## Estrutura

```text
index.html
gerar_manifesto.py
dados/
  clientes.xlsx
  vendas.xlsx
  importados/
    manifest.json
    qualquer-lista-1.xlsx
    qualquer-lista-2.xlsx
.github/
  workflows/
    atualizar-importados.yml
```

## Atualizações normais

### Base de clientes
Substituir apenas:

`dados/clientes.xlsx`

### Vendas
Substituir apenas:

`dados/vendas.xlsx`

### Novas listas para comparar
Adicionar cada novo ficheiro Excel ou CSV dentro de:

`dados/importados/`

Não é necessário alterar o `index.html`.

A GitHub Action atualiza automaticamente o `manifest.json`. Depois, cada ficheiro aparece como um separador próprio no dashboard, com:

- comparação própria contra a base de clientes;
- indicadores próprios;
- mapa próprio;
- lista própria;
- filtros próprios.

Os ficheiros importados nunca são misturados entre si.

## Regras

- `Gr.Empresa = INA`: cliente inativo.
- Os inativos aparecem a vermelho e ficam fora das contagens de ativos.
- A base de clientes tem o seu próprio mapa.
- Cada ficheiro importado tem um mapa independente.
- As listas importadas são sempre comparadas com `clientes.xlsx`.
- A comparação usa NIF como chave principal, depois email e nome.
- Os valores de vendas não são mostrados.
- `vendas.xlsx` serve apenas para assinalar se o cliente tem vendas.

## GitHub Pages e Actions

1. Carregar todo o conteúdo para a branch `main`.
2. Em **Settings → Pages**, publicar a partir da branch `main`, pasta `/root`.
3. Em **Settings → Actions → General → Workflow permissions**, selecionar:
   **Read and write permissions**.
4. Sempre que adicionar ou remover ficheiros em `dados/importados`, a Action atualiza o manifesto.

## Privacidade

Num GitHub Pages público, os Excel ficam acessíveis por URL. Para dados pessoais reais, deve usar autenticação e armazenamento privado.

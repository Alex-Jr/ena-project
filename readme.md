# ENA-PROJECT

Scripts para auxiliar atividades administrativas do ENA.

## Instalação

Usar [pip](https://pip.pypa.io/en/stable/) para instalar dependências.

```bash
pip install -r requirements.txt
```

## Uso

Nessa mesma pasta criar um arquivo players-ids.txt contendo um ID de jogador que você deseja gerar dados sobre a sky hero. **Não deixar nenhuma linha vazia**  
Exemplo
```
123456
123457
```

Com python executar
```bash
python3 generate-sky-hero.py 
```

Isso gerará um arquivo generate-sky-hero-output.csv contendo o nome e quantidade de medalhas de cada jogador.
Exemplo
```
jogador legal: 12
jogador chato: 0
```

## License
[GNU AGPLv3](https://choosealicense.com/licenses/agpl-3.0/)
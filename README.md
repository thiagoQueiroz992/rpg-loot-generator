# rpg-loot-generator
Esse projeto representa a lógica por trás de um sistema de geração de loot aleatório comum em jogos de RPG.

---

## Explicando

- Ele usa informações de uma tabela de loots (loot table) que contém todos os itens possíveis de serem gerados no loot.
- Essa tabela armazena o nome de cada item, a chance de ser gerado e a quantidade mínima e máxima na qual pode ser gerado.
- O código faz com que cada item tente ser gerado uma vez, e a chance de ser gerado ou não vai depender do valor armazenado na tabela de loot.
- O código também define a quantidade na qual o item vai ser gerado, baseado na quantida mínima e máxima possível armazenada na tabela de loot, caso o item seja gerado.
- Após todos os itens terem tido suas tentativas de serem gerados, o código exibe quais itens foram gerados no loot e a quantidade deles.
---

Fiz esse projeto para tentar entender a lógica por trás de sistemas de looting em jogos como Minecraft, Terraria, Genshin Impact entre outros. Espero que gostem!

---

export const hh3Terms = {
  "AFK": "Away From Keyboard. In this guide, it refers to players sitting in the AFK zone instead of actively playing.",
  "AFK zone": "The area where inactive players can stay. Community reports say AFK players can increase farming multipliers for active players.",
  "Booster": "A purchasable bonus or modifier that improves a run or changes rewards.",
  "Delist": "Remove a rarity from the current loot pool.",
  "Farming": "Repeating a route or activity to earn money, rewards, or progression faster.",
  "Killstreak": "A running bonus tied to continuous eliminations.",
  "Loot pool": "The group of items or rarities currently available to drop or appear.",
  "Mythic": "A high-tier weapon rarity.",
  "Prestige": "A reset system that clears some progress while keeping certain long-term investments.",
  "Rescue": "Saving a hostage or trapped character during a run for added rewards and multiplier value.",
  "Roguelike": "A run-based game style where progress often builds over repeated attempts, and each run can reset short-term progress while improving long-term progression.",
  "Run": "One full attempt through the hotel.",
  "Soap": "A currency used for progression, including unlocking and upgrading weapon classes.",
  "Unbreakable killstreak": "A booster that protects your killstreak so it does not reset as easily during farming."
} as const;

export type HH3TermName = keyof typeof hh3Terms;

import os.path
from collections import defaultdict

import numpy as np

from colorFromImage import averageColorFromFileName
from extractMaterialNames import materialNamesFromFile
from hashString import hashStringLikeJava


def switchFileName(material: str):
    material = material.lower()
    existsFileName = textureFolderName + 'block/' + material + '.png'
    if not os.path.exists(existsFileName):
        existsFileName = textureFolderName + 'block/' + material + '_top.png'
    if not os.path.exists(existsFileName):
        existsFileName = textureFolderName + 'block/' + material + '_back.png'
    if not os.path.exists(existsFileName):
        existsFileName = textureFolderName + 'block/' + material + '_front.png'
    if not os.path.exists(existsFileName):
        existsFileName = textureFolderName + 'block/' + material + '_still.png'
    if not os.path.exists(existsFileName):
        existsFileName = textureFolderName + 'item/' + material + '_00.png'
    if not os.path.exists(existsFileName):
        existsFileName = textureFolderName + 'item/' + material + '.png'

    if not os.path.exists(existsFileName):
        raise FileNotFoundError(existsFileName)
    return existsFileName


# we're generating rainbow

# extract from minecraft jar
textureFolderName = 'textures/textures1214/'
# f12 fetch from spigot https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html
allMaterials = materialNamesFromFile('materialsFromSpigotAPI1214.html')

specificContains: list[tuple[str, np.array]] = [

    ('_BANNER_PATTERN', averageColorFromFileName(switchFileName('CREEPER_BANNER_PATTERN'))),
    ('_POTTERY_SHERD', averageColorFromFileName(switchFileName('SCRAPE_POTTERY_SHERD'))),

    ('SLIME', averageColorFromFileName(switchFileName('SLIME_BLOCK'))),
    ('WITHER', np.array([0x39, 0x39, 0x39])),
    ('ZOMBIE',averageColorFromFileName(textureFolderName + 'entity/zombie/zombie.png', startX=8, endX=16, startY=8, endY=16)),
    ('PLAYER', averageColorFromFileName(textureFolderName + 'entity/player/wide/steve.png', startX=8, endX=16, startY=8,endY=16)),
    ('CREEPER',averageColorFromFileName(textureFolderName + 'entity/creeper/creeper.png', startX=8, endX=16, startY=8, endY=16)),
    ('SKELETON',averageColorFromFileName(textureFolderName + 'entity/skeleton/skeleton.png', startX=8, endX=16, startY=8,endY=16)),
    ('PIGLIN',averageColorFromFileName(textureFolderName + 'entity/piglin/piglin.png', startX=8, endX=16, startY=8,endY=16)),
    ('PHANTOM',averageColorFromFileName(textureFolderName + 'entity/phantom.png', startX=6, endX=13, startY=6,endY=9)),
    ('BEE_',averageColorFromFileName(switchFileName('HONEY_BLOCK'))),
    ('BEEHIVE',averageColorFromFileName(switchFileName('HONEY_BLOCK'))),
    ('BREEZE',averageColorFromFileName(textureFolderName + 'entity/breeze/breeze.png', startX=8, endX=16, startY=8, endY=16)),
    ('GOAT',averageColorFromFileName(textureFolderName + 'entity/goat/goat.png', startX=17, endX=27, startY=17,endY=28)),

    ('MUSIC_DISC_', averageColorFromFileName(textureFolderName + 'item/music_disc_precipice.png')),
    ('LEGACY_RECORD', averageColorFromFileName(textureFolderName + 'item/music_disc_precipice.png')),
    ('DISC_FRAGMENT_5', averageColorFromFileName(textureFolderName + 'item/music_disc_precipice.png')),
    ('CANDLE', averageColorFromFileName(textureFolderName + 'item/candle.png')),
    ('LEGACY_EXP_BOTTLE', averageColorFromFileName(switchFileName('EXPERIENCE_BOTTLE'))),
    ('END_STONE', averageColorFromFileName(textureFolderName + 'block/end_stone.png')),
    ('PRISMARINE', averageColorFromFileName(textureFolderName + 'item/prismarine_shard.png')),
    ('MELON', averageColorFromFileName(textureFolderName + 'block/melon_top.png')),
    ('DARK_OAK', averageColorFromFileName(textureFolderName + 'block/dark_oak_planks.png')),
    ('WOODEN_', averageColorFromFileName(textureFolderName + 'block/oak_planks.png')),
    ('ICE', averageColorFromFileName(textureFolderName + 'block/ice.png')),
    ('HONEY', averageColorFromFileName(textureFolderName + 'item/honeycomb.png')),
    ('_LEAVES', np.array([0x59, 0xae, 0x30])),
    ('COAL', np.array([0x39, 0x39, 0x39])),
    ('BLACK_', np.array([0x39, 0x39, 0x39])),
    ('ANCIENT_DEBRIS', np.array([87, 56, 48])),
    ('DIAMOND', averageColorFromFileName(textureFolderName + 'item/diamond.png')),
    ('REDSTONE', averageColorFromFileName(textureFolderName + 'block/redstone_block.png')),
    ('LAPIS', averageColorFromFileName(textureFolderName + 'item/lapis_lazuli.png')),
    ('LIGHT_GRAY', averageColorFromFileName(textureFolderName + 'item/light_gray_dye.png')),
    ('ARROW', np.array([0xa0, 0xa0, 0xa0])),
    ('GRASS', np.array([0x79, 0xc0, 0x5a])),
    ('QUARTZ', averageColorFromFileName(textureFolderName + 'item/quartz.png')),
    ('AMETHYST', averageColorFromFileName(textureFolderName + 'item/amethyst_shard.png')),
    ('COPPER', averageColorFromFileName(textureFolderName + 'item/copper_ingot.png')),
    ('SPONGE', averageColorFromFileName(textureFolderName + 'block/sponge.png')),
    ('PODZOL', averageColorFromFileName(textureFolderName + 'block/podzol_top.png')),
    ('MOSS_', averageColorFromFileName(textureFolderName + 'block/moss_block.png')),
    ('MOSSY_', averageColorFromFileName(textureFolderName + 'block/moss_block.png')),
    ('BOWL', averageColorFromFileName(textureFolderName + 'item/bowl.png')),
    ('PITCHER', averageColorFromFileName(switchFileName('PITCHER_CROP'))),
    ('BOOKSHELF', averageColorFromFileName(textureFolderName + 'block/bookshelf.png')),
    ('DRIPLEAF', averageColorFromFileName(textureFolderName + 'block/big_dripleaf_top.png')),
    ('CHORUS', averageColorFromFileName(switchFileName("PURPUR_BLOCK"))),
    ('DRAGON', averageColorFromFileName(switchFileName("PURPUR_BLOCK"))),
    ('PURPUR', averageColorFromFileName(textureFolderName + 'block/purpur_block.png')),
    ('SOUL_SAND', averageColorFromFileName(textureFolderName + 'block/soul_sand.png')),
    ('SOUL_SOIL', averageColorFromFileName(textureFolderName + 'block/soul_sand.png')),
    ('SOUL_', averageColorFromFileName(textureFolderName + 'block/soul_fire_0.png')),
    ('LEGACY_SOIL', averageColorFromFileName(textureFolderName + 'block/dirt.png')),
    ('PUMPKIN', averageColorFromFileName(textureFolderName + 'block/pumpkin_top.png')),
    ('GLOWSTONE', averageColorFromFileName(textureFolderName + 'block/glowstone.png')),
    ('ENDER', averageColorFromFileName(textureFolderName + 'item/ender_pearl.png')),
    ('END_', averageColorFromFileName(textureFolderName + 'item/ender_pearl.png')),
    ('SHIELD', averageColorFromFileName(textureFolderName + 'block/oak_planks.png')),
    ('LEGACY_SEEDS', averageColorFromFileName(textureFolderName + 'item/wheat.png')),
    ('WHEAT', averageColorFromFileName(textureFolderName + 'item/wheat.png')),
    ('BREAD', averageColorFromFileName(textureFolderName + 'item/bread.png')),
    ('BEETROOT', averageColorFromFileName(textureFolderName + 'item/beetroot.png')),
    ('NETHER_WART', averageColorFromFileName(textureFolderName + 'item/nether_wart.png')),
    ('BONE', averageColorFromFileName(textureFolderName + 'item/bone.png')),
    ('MAGMA', averageColorFromFileName(textureFolderName + 'block/magma.png')),
    ('BLACKSTONE', averageColorFromFileName(textureFolderName + 'block/blackstone.png')),
    ('GOLDEN_', averageColorFromFileName(textureFolderName + 'block/gold_block.png')),
    ('CLOCK', averageColorFromFileName(textureFolderName + 'block/gold_block.png')),
    ('APPLE', averageColorFromFileName(textureFolderName + 'item/apple.png')),
    ('HEAVY_WEIGHTED_PRESSURE_PLATE', averageColorFromFileName(textureFolderName + 'block/gold_block.png')),
    ('LIGHT_WEIGHTED_PRESSURE_PLATE', averageColorFromFileName(textureFolderName + 'block/iron_block.png')),
    ('WATER', np.array([0x3f, 0x76, 0xe4])),
    ('LAVA', averageColorFromFileName(textureFolderName + 'block/lava_still.png')),
    ('MILK', averageColorFromFileName(textureFolderName + 'item/bone.png')),
    ('BUCKET', averageColorFromFileName(textureFolderName + 'item/bucket.png')),
    ('POTION', averageColorFromFileName(textureFolderName + 'block/glass.png')),
    ('_AIR', np.array([0xa0, 0xa0, 0xa0])),
    ('OBSIDIAN', averageColorFromFileName(textureFolderName + 'block/obsidian.png')),
    ('RED_NETHER_BRICK', averageColorFromFileName(textureFolderName + 'block/red_nether_bricks.png')),
    ('DECORATED_POT', averageColorFromFileName(textureFolderName + 'entity/decorated_pot/decorated_pot_base.png')),
    ('OXEYE_DAISY', averageColorFromFileName(switchFileName('OXEYE_DAISY'))),
    ('CARROT', averageColorFromFileName(switchFileName('CARROT'))),
    ('POTATO', averageColorFromFileName(switchFileName('POTATO'))),
    ('COCOA', averageColorFromFileName(switchFileName('COCOA_BEANS'))),
    ('LEGACY_WOOD', averageColorFromFileName(textureFolderName + 'block/oak_planks.png')),
    ('LEGACY_DIODE', averageColorFromFileName(switchFileName('REDSTONE'))),
    ('LEGACY_COMMAND', averageColorFromFileName(switchFileName('COMMAND_BLOCK'))),
    ('TRIPWIRE', averageColorFromFileName(switchFileName('IRON_INGOT'))),
    ('WEEPING_VINES', averageColorFromFileName(switchFileName('CRIMSON_PLANKS'))),
    ('DRIED_KELP', averageColorFromFileName(textureFolderName + 'item/dried_kelp.png')),
    ('KELP', averageColorFromFileName(textureFolderName + 'item/kelp.png')),

    ('SPIDER_EYE', averageColorFromFileName(switchFileName('FERMENTED_SPIDER_EYE'))),
]
defined: list[tuple[str, np.array]] = [
    ('AIR', np.array([0xa0, 0xa0, 0xa0])),
    ('FIRE', averageColorFromFileName(textureFolderName + 'block/fire_0.png')),
    ('LEGACY_FIRE', averageColorFromFileName(textureFolderName + 'block/fire_0.png')),
    ('LEGACY_LOG', averageColorFromFileName(textureFolderName + 'block/oak_planks.png')),
    ('LEGACY_LOG_2', averageColorFromFileName(textureFolderName + 'block/oak_planks.png')),
    ('LEGACY_BED_BLOCK', averageColorFromFileName(switchFileName('RED_WOOL'))),
    ('LEGACY_BED', averageColorFromFileName(switchFileName('RED_WOOL'))),
    ('LEGACY_SAPLING', averageColorFromFileName(textureFolderName + 'block/oak_planks.png')),
    ('LEGACY_STEP', averageColorFromFileName(textureFolderName + 'block/oak_planks.png')),
    ('LEGACY_DOUBLE_STEP', averageColorFromFileName(textureFolderName + 'block/oak_planks.png')),
    ('LEGACY_SIGN_POST', averageColorFromFileName(textureFolderName + 'block/oak_planks.png')),
    ('LEGACY_WALL_SIGN', averageColorFromFileName(textureFolderName + 'block/oak_planks.png')),
    ('LEGACY_TRAP_DOOR', averageColorFromFileName(textureFolderName + 'block/oak_planks.png')),
    ('LEGACY_MUSHROOM_SOUP', averageColorFromFileName(textureFolderName + 'block/oak_planks.png')),
    ('LEGACY_SIGN', averageColorFromFileName(textureFolderName + 'block/oak_planks.png')),
    ('LEGACY_BOAT', averageColorFromFileName(textureFolderName + 'block/oak_planks.png')),
    ('LEGACY_FENCE', averageColorFromFileName(textureFolderName + 'block/oak_planks.png')),
    ('LEGACY_FENCE_GATE', averageColorFromFileName(textureFolderName + 'block/oak_planks.png')),
    ('LEGACY_SMOOTH_STAIRS', averageColorFromFileName(textureFolderName + 'block/stone.png')),
    ('LEGACY_COBBLE_WALL', averageColorFromFileName(textureFolderName + 'block/cobblestone.png')),
    ('LEVER', averageColorFromFileName(textureFolderName + 'block/cobblestone.png')),
    ('LEGACY_LEVER', averageColorFromFileName(textureFolderName + 'block/cobblestone.png')),
    ('LEGACY_NETHER_FENCE', averageColorFromFileName(textureFolderName + 'block/nether_bricks.png')),
    ('LEGACY_WORKBENCH', averageColorFromFileName(switchFileName('CRAFTING_TABLE'))),
    ('LEGACY_WOOL', averageColorFromFileName(switchFileName('WHITE_WOOL'))),
    ('LEGACY_BANNER', averageColorFromFileName(switchFileName('WHITE_WOOL'))),
    ('LEGACY_CARPET', averageColorFromFileName(switchFileName('WHITE_WOOL'))),
    ('LEGACY_WALL_BANNER', averageColorFromFileName(switchFileName('WHITE_WOOL'))),
    ('LEGACY_STANDING_BANNER', averageColorFromFileName(switchFileName('WHITE_WOOL'))),
    ('LEGACY_CONCRETE', averageColorFromFileName(switchFileName('WHITE_WOOL'))),
    ('LEGACY_CONCRETE_POWDER', averageColorFromFileName(switchFileName('WHITE_WOOL'))),
    ('LEGACY_WEB', averageColorFromFileName(switchFileName('COBWEB'))),
    ('COBWEB', averageColorFromFileName(switchFileName('COBWEB'))),
    ('LEGACY_PORTAL', averageColorFromFileName(switchFileName('NETHER_PORTAL'))),
    ('LEGACY_CROPS', averageColorFromFileName(switchFileName('WHEAT'))),
    ('LEGACY_HUGE_MUSHROOM_1', averageColorFromFileName(switchFileName('BROWN_WOOL'))),
    ('LEGACY_HUGE_MUSHROOM_2', averageColorFromFileName(switchFileName('BROWN_WOOL'))),
    ('LEGACY_SKULL', averageColorFromFileName(textureFolderName + 'entity/skeleton/skeleton.png', startX=8, endX=16, startY=8,endY=16)),
    ('LEGACY_DOUBLE_PLANT', np.array([0x79, 0xc0, 0x5a])),
    ('TORCH', np.array([255, 216, 0])),
    ('WALL_TORCH', np.array([255, 216, 0])),
    ('LEGACY_TORCH', np.array([255, 216, 0])),

    ('LEGACY_ENCHANTMENT_TABLE', averageColorFromFileName(switchFileName('RESPAWN_ANCHOR'))),
    ('ENCHANTING_TABLE', averageColorFromFileName(switchFileName('RESPAWN_ANCHOR'))),
    ('RESPAWN_ANCHOR', averageColorFromFileName(switchFileName('RESPAWN_ANCHOR'))),

    ('LEGACY_WATCH', averageColorFromFileName(switchFileName('CLOCK'))),
    ('LEGACY_COOKED_FISH', averageColorFromFileName(switchFileName('CLOCK'))),
    ('LEGACY_RAW_FISH', np.array([104,157,143])),

    ('LEGACY_GRILLED_PORK', averageColorFromFileName(switchFileName('COOKED_PORKCHOP'))),
    ('LEGACY_PORK', averageColorFromFileName(switchFileName('PORKCHOP'))),

    ('LEGACY_SULPHUR', averageColorFromFileName(switchFileName('GUNPOWDER'))),
    ('FLOWER_POT', averageColorFromFileName(switchFileName('BRICKS'))),
    ('LEGACY_FLOWER_POT', averageColorFromFileName(switchFileName('BRICKS'))),
    ('LEGACY_FLOWER_POT_ITEM', averageColorFromFileName(switchFileName('BRICKS'))),

    ('LEGACY_FIREBALL', averageColorFromFileName(switchFileName('FIRE_CHARGE'))),
    ('LEGACY_FIREWORK', averageColorFromFileName(switchFileName('FIRE_CHARGE'))),
    ('FIREWORK_ROCKET', averageColorFromFileName(switchFileName('FIRE_CHARGE'))),
    ('LEGACY_FIREWORK_CHARGE', averageColorFromFileName(switchFileName('FIRE_CHARGE'))),

    ('LEGACY_LEASH', averageColorFromFileName(switchFileName('SLIME_BLOCK'))),

    ('DANDELION', averageColorFromFileName(switchFileName('YELLOW_DYE'))),
    ('SUNFLOWER', averageColorFromFileName(switchFileName('YELLOW_DYE'))),
    ('POTTED_DANDELION', averageColorFromFileName(switchFileName('YELLOW_DYE'))),
    ('POPPY', averageColorFromFileName(switchFileName('RED_DYE'))),
    ('CORNFLOWER', averageColorFromFileName(switchFileName('BLUE_DYE'))),
    ('POTTED_POPPY', averageColorFromFileName(switchFileName('RED_DYE'))),
    ('POTTED_CORNFLOWER', averageColorFromFileName(switchFileName('BLUE_DYE'))),
    ('NETHER_SPROUTS', averageColorFromFileName(switchFileName('WARPED_PLANKS'))),
    ('LEGACY_MYCEL', averageColorFromFileName(switchFileName('MYCELIUM'))),
    ('LEGACY_NETHER_STALK', averageColorFromFileName(switchFileName('NETHER_WART'))),
    ('LEGACY_SKULL_ITEM', averageColorFromFileName(textureFolderName + 'item/bone.png')),

    ('CHEST', averageColorFromFileName(textureFolderName + 'block/oak_planks.png')),
    ('LEGACY_CHEST', averageColorFromFileName(textureFolderName + 'block/oak_planks.png')),
    ('TRAPPED_CHEST', averageColorFromFileName(textureFolderName + 'block/oak_planks.png')),
    ('LEGACY_TRAPPED_CHEST', averageColorFromFileName(textureFolderName + 'block/oak_planks.png')),

    ('LEGACY_BOAT_SPRUCE', averageColorFromFileName(textureFolderName + 'block/spruce_planks.png')),
    ('LEGACY_BOAT_BIRCH', averageColorFromFileName(textureFolderName + 'block/birch_planks.png')),
    ('LEGACY_BOAT_JUNGLE', averageColorFromFileName(textureFolderName + 'block/jungle_planks.png')),
    ('LEGACY_BOAT_ACACIA', averageColorFromFileName(textureFolderName + 'block/acacia_planks.png')),
    ('LEGACY_TOTEM', averageColorFromFileName(switchFileName('TOTEM_OF_UNDYING'))),
    ('SWEET_BERRY_BUSH', averageColorFromFileName(textureFolderName + 'block/sweet_berry_bush_stage1.png')),

    ('GHAST_TEAR', averageColorFromFileName(switchFileName('GLASS'))),
    ('LEGACY_GHAST_TEAR', averageColorFromFileName(switchFileName('GLASS'))),
    ('LIGHTNING_ROD', averageColorFromFileName(switchFileName('COPPER_INGOT'))),
    ('LIGHT', averageColorFromFileName(switchFileName('LIGHT'))),
    ('BLAZE_ROD', averageColorFromFileName(switchFileName('LAVA'))),
    ('LEGACY_BLAZE_ROD', averageColorFromFileName(switchFileName('LAVA'))),
]
specificContainsMap: dict[str, np.ndarray[int]] = {}
meetEndings: list[str] = ['_PLANKS', '_INGOT', '_SHARD', '_WEB', '_SCRAP',
                          '_WOOL',# 16 colors
                          '_CORAL_BLOCK',
                          '_SCUTE', '_ARMOR_TRIM_SMITHING_TEMPLATE',
                          ]
meetEquals: list[str] = ['SPYGLASS', 'TINTED_GLASS', 'GLASS',
                         'LEATHER', 'ANDESITE', 'BOW', 'ARMOR_STAND', 'SAND',
                         'STRING', 'STONE', 'GRANITE', 'DEEPSLATE', 'DIORITE', 'TUFF', 'CALCITE',
                         'DIRT', 'EMERALD', 'MUD', 'BEDROCK', 'GRAVEL', 'ALLIUM', 'SEA_PICKLE', 'AZURE_BLUET',
                         'DEAD_BUSH', 'OXEYE_DAISY', 'LILY_OF_THE_VALLEY',
                         'SUGAR_CANE', 'SPORE_BLOSSOM', 'TWISTING_VINES',
                         'TORCHFLOWER', 'HANGING_ROOTS', 'BAMBOO',
                         'END_ROD', 'FARMLAND', 'LADDER', 'SNOW', 'NETHERRACK', 'BASALT',
                         'FURNACE', 'CACTUS', 'CLAY', 'JUKEBOX', 'JACK_O_LANTERN', 'MUSHROOM_STEM', 'CHAIN',
                         'SPAWNER', 'CRAFTING_TABLE', 'VINE', 'GLOW_LICHEN', 'MYCELIUM', 'LILY_PAD',
                         'SCULK', 'COMMAND_BLOCK', 'BEACON', 'ANVIL', 'TERRACOTTA',
                         'LILAC', 'ROSE_BUSH', 'PEONY', 'SHULKER_BOX', 'HEAVY_CORE', 'FERN', 'AZALEA',
                         'TNT', 'TURTLE_EGG', 'SNIFFER_EGG', 'REPEATER', 'COMPARATOR', 'PISTON',
                         'BARRIER', 'HOPPER', 'DISPENSER', 'DROPPER', 'LECTERN', 'TARGET',
                         'SEA_LANTERN', 'STRUCTURE_VOID', 'CONDUIT', 'SCAFFOLDING', 'OBSERVER',
                         'DAYLIGHT_DETECTOR', 'HAY_BLOCK', 'NOTE_BLOCK', 'MUSHROOM_STEW',
                         'ACTIVATOR_RAIL', 'RAIL', 'SADDLE', 'MINECART', 'CARROT_ON_A_STICK', 'ELYTRA',
                         'STRUCTURE_BLOCK', 'FLINT', 'COOKED_PORKCHOP', 'PORKCHOP', 'GUNPOWDER', 'FEATHER',
                         'JIGSAW', 'RAW_IRON', 'RAW_GOLD', 'RAW_COPPER', 'POTATO', 'MAP',
                         'STICK', 'PAINTING', 'PAPER', 'BOOK', 'EGG', 'RECOVERY_COMPASS', 'COMPASS',
                         'COD', 'SALMON', 'TROPICAL_FISH', 'PUFFERFISH', 'SUGAR', 'CAKE', 'COOKIE', 'CRAFTER', 'SHEARS',
                         'BEEF', 'ROTTEN_FLESH', 'CHICKEN', 'GLOW_INK_SAC',
                         'INK_SAC', 'NETHER_BRICK', 'BRICK', 'WOLF_ARMOR',
                         'BUNDLE', 'FISHING_ROD', 'BLAZE_POWDER', 'BREWING_STAND', 'CAULDRON', 'EXPERIENCE_BOTTLE',
                         'WIND_CHARGE', 'MACE', 'ITEM_FRAME', 'GLOW_ITEM_FRAME', 'CARROT', 'NETHER_STAR',
                         'FIREWORK_STAR', 'RABBIT', 'TOTEM_OF_UNDYING', 'SHULKER_SHELL',
                         'MUTTON', 'LEAD', 'NAME_TAG', 'TRIDENT','NAUTILUS_SHELL',
                         'BELL', 'LANTERN', 'SWEET_BERRIES', 'GLOW_BERRIES','CARTOGRAPHY_TABLE', 'FLETCHING_TABLE',
                         'SMITHING_TABLE', 'CAMPFIRE','HEART_OF_THE_SEA', 'SUSPICIOUS_STEW','BARREL',
                         'SMOKER', 'COMPOSTER', 'FROGSPAWN', 'BRUSH', 'TRIAL_KEY',
                         'NETHER_PORTAL','OMINOUS_BOTTLE', 'LOOM', 'VAULT','SHROOMLIGHT',
                         'OCHRE_FROGLIGHT', 'VERDANT_FROGLIGHT', 'PEARLESCENT_FROGLIGHT',
                         ]
meetEquals.sort(key=lambda a: len(a), reverse=True)

materialMappings = defaultdict(list)
print(allMaterials)
for materialName in allMaterials:
    materialName = materialName.replace('LEGACY_', '')
    matchedFlag = False
    for specificContain in specificContains:
        if specificContain[0] in materialName:
            matchedFlag = True
            break
    if matchedFlag:
        continue
    for expectEnding in meetEndings:
        if materialName.endswith(expectEnding):
            imgNameToExtract = switchFileName(materialName)
            try:
                avgColor = averageColorFromFileName(imgNameToExtract)
            except Exception as e:
                print(imgNameToExtract)
                raise e
            specificContains.append((materialName[:(-1) * len(expectEnding)] + '_', avgColor))

for expectEqual in meetEquals:
    imgNameToExtract = switchFileName(expectEqual)
    try:
        avgColor = averageColorFromFileName(imgNameToExtract)
    except Exception as e:
        print(imgNameToExtract)
        raise e
    specificContains.append((expectEqual, avgColor))

for specificContain in specificContains:
    specificContainsMap[specificContain[0]] = specificContain[1]

satisfiedCounter = 0
notFounds = []
for materialName in allMaterials:
    foundFlag = False
    if materialName in meetEquals:
        materialMappings[materialName].append(materialName)
        satisfiedCounter += 1
        continue

    for specificContain in specificContains:
        if specificContain[0] in materialName:
            materialMappings[specificContain[0]].append(materialName)
            satisfiedCounter += 1
            foundFlag = True
            break
    if not foundFlag:
        notFounds.append(materialName)

for i in defined:
    if not i[0] in notFounds:
        raise ModuleNotFoundError(i[0])
    specificContainsMap[i[0]] = i[1]
    materialMappings[i[0]].append(i[0])
    satisfiedCounter += 1
    notFounds.remove(i[0])

cannotFindColor = []

materialToPut:list[tuple[str,str]] = []
legacyMaterialToPut:list[tuple[str,str]] = []
for k in materialMappings.keys():
    try:
        colorR = specificContainsMap[k][0]
        colorG = specificContainsMap[k][1]
        colorB = specificContainsMap[k][2]
        print('\033[38;2;%d;%d;%dm%s %s\033[0m' % (
            colorR, colorG, colorB, k, materialMappings[k]))
        for m in materialMappings[k]:
            colorStringR = hex(colorR)[2:]
            if len(colorStringR) < 2:
                colorStringR = '0'+colorStringR
            colorStringG = hex(colorG)[2:]
            if len(colorStringG) < 2:
                colorStringG = '0'+colorStringG
            colorStringB = hex(colorB)[2:]
            if len(colorStringB) < 2:
                colorStringB = '0'+colorStringB
            colorString = '#'+colorStringR+colorStringG+colorStringB
            if m.startswith('LEGACY_'):
                m = m[7:]
                legacyMaterialToPut.append((m,colorString))
            else:
                materialToPut.append((m, colorString))
    except Exception as e:
        if specificContainsMap[k] is None:
            cannotFindColor.append(k)
        else:
            print(k, specificContainsMap[k])
            raise e

print('satisfied/total:%d/%d' % (satisfiedCounter, len(allMaterials)))
# print(notFounds)
# print(cannotFindColor)
materialToPut.sort(key=lambda m:hashStringLikeJava(m[0]))
legacyMaterialToPut.sort(key=lambda m:hashStringLikeJava(m[0]))
print(materialToPut)
print(legacyMaterialToPut)


#collision test
for l in [materialToPut,legacyMaterialToPut]:
    hashSet:set[int] = set()
    collisions = 0
    for s in l:
        hashed = hashStringLikeJava(s[0])
        if hashed in hashSet:
            collisions += 1
        else:
            hashSet.add(hashed)
    print('collisions:%d'%collisions)

with open('materialColorMap',mode='w') as f:
    print('materialToPut size:%d'%len(materialToPut))
    for m in materialToPut:
        f.write('put("%s",net.md_5.bungee.api.ChatColor.of("%s"));\n'%m)
with open('legacyMaterialColorMap',mode='w') as f:
    print('legacyMaterialToPut size:%d'%len(legacyMaterialToPut))
    for m in legacyMaterialToPut:
        f.write('put("%s",net.md_5.bungee.api.ChatColor.of("%s"));\n'%m)

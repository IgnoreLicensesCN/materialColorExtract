import os.path
from collections import defaultdict
import cv2, numpy as np
from sklearn.cluster import KMeans
from extractMaterialNames import materialNamesFromFile
from colorFromImage import averageColorFromFileName


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
    ('MUSIC_DISC_', averageColorFromFileName(textureFolderName + 'item/music_disc_precipice.png')),
    ('LEGACY_RECORD', averageColorFromFileName(textureFolderName + 'item/music_disc_precipice.png')),
    ('END_STONE', averageColorFromFileName(textureFolderName + 'block/end_stone.png')),
    ('PRISMARINE', averageColorFromFileName(textureFolderName + 'item/prismarine_shard.png')),
    ('MELON', averageColorFromFileName(textureFolderName + 'block/melon_top.png')),
    ('DARK_OAK', averageColorFromFileName(textureFolderName + 'block/dark_oak_planks.png')),
    ('WOODEN_', averageColorFromFileName(textureFolderName + 'block/oak_planks.png')),
    ('ICE', averageColorFromFileName(textureFolderName + 'block/ice.png')),
    ('HONEY', averageColorFromFileName(textureFolderName + 'item/honeycomb.png')),
    ('_LEAVES', np.array([0x59, 0xae, 0x30])),
    ('SKELETON', averageColorFromFileName(textureFolderName + 'item/bone.png')),
    ('WITHER', np.array([0x39, 0x39, 0x39])),
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
    # ('NETHER_BRICK', averageColorFromFileName(textureFolderName + 'item/nether_brick.png')),
    # ('BRICK', averageColorFromFileName(textureFolderName + 'item/brick.png')),
    ('BOOKSHELF', averageColorFromFileName(textureFolderName + 'block/bookshelf.png')),
    ('DRIPLEAF', averageColorFromFileName(textureFolderName + 'block/big_dripleaf_top.png')),
    ('CHORUS', averageColorFromFileName(textureFolderName + 'item/chorus_fruit.png')),
    ('PURPUR', averageColorFromFileName(textureFolderName + 'block/purpur_block.png')),
    ('SOUL_SAND', averageColorFromFileName(textureFolderName + 'block/soul_sand.png')),
    ('SOUL_SOIL', averageColorFromFileName(textureFolderName + 'block/soul_sand.png')),
    ('SOUL_', averageColorFromFileName(textureFolderName + 'block/soul_fire_0.png')),
    ('LEGACY_SOIL', averageColorFromFileName(textureFolderName + 'block/dirt.png')),
    ('PUMPKIN', averageColorFromFileName(textureFolderName + 'block/pumpkin_top.png')),
    ('GLOWSTONE', averageColorFromFileName(textureFolderName + 'block/glowstone.png')),
    ('ENDER', averageColorFromFileName(textureFolderName + 'item/ender_pearl.png')),
    ('END_', averageColorFromFileName(textureFolderName + 'item/ender_pearl.png')),
    ('DRAGON_EGG', averageColorFromFileName(textureFolderName + 'item/ender_pearl.png')),
    ('CHEST', averageColorFromFileName(textureFolderName + 'block/oak_planks.png')),
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
    ('OBSIDIAN', averageColorFromFileName(textureFolderName + 'block/obsidian.png')),
    ('RED_NETHER_BRICK', averageColorFromFileName(textureFolderName + 'block/red_nether_bricks.png')),
    ('DECORATED_POT', averageColorFromFileName(textureFolderName + 'entity/decorated_pot/decorated_pot_base.png')),
    ('OXEYE_DAISY', averageColorFromFileName(switchFileName('OXEYE_DAISY'))),
    ('CARROT', averageColorFromFileName(switchFileName('CARROT'))),
    ('POTATO', averageColorFromFileName(switchFileName('POTATO'))),
    # ('AIR', np.array([0xa0, 0xa0, 0xa0])),
]
specificContainsMap: dict[[str, np.array]] = {}
meetEndings: list[str] = ['_PLANKS', '_INGOT', '_SHARD', '_WEB', '_SCRAP', '_DYE', '_POTTERY_SHERD', '_CORAL_BLOCK',
                          '_SCUTE', '_ARMOR_TRIM_SMITHING_TEMPLATE',
                          ]
meetEquals: list[str] = ['SPYGLASS', 'TINTED_GLASS', 'GLASS',
                         'LEATHER', 'ANDESITE', 'BOW', 'ARMOR_STAND', 'SAND',
                         'STRING', 'COBWEB', 'STONE', 'GRANITE', 'DEEPSLATE', 'DIORITE', 'TUFF', 'CALCITE',
                         'DIRT', 'EMERALD', 'MUD', 'BEDROCK', 'GRAVEL', 'ALLIUM', 'SEA_PICKLE', 'AZURE_BLUET',
                         'DEAD_BUSH', 'DANDELION', 'POPPY', 'OXEYE_DAISY', 'CORNFLOWER', 'LILY_OF_THE_VALLEY',
                         'SUGAR_CANE', 'SPORE_BLOSSOM', 'NETHER_SPROUTS', 'WEEPING_VINES', 'TWISTING_VINES', 'KELP',
                         'TORCHFLOWER', 'PITCHER_PLANT', 'HANGING_ROOTS', 'BAMBOO',
                         'TORCH', 'END_ROD', 'FARMLAND', 'LADDER', 'SNOW', 'NETHERRACK', 'BASALT',
                         'FURNACE', 'CACTUS', 'CLAY', 'JUKEBOX', 'JACK_O_LANTERN', 'MUSHROOM_STEM', 'CHAIN',
                         'SPAWNER', 'CRAFTING_TABLE', 'VINE', 'GLOW_LICHEN', 'MYCELIUM', 'LILY_PAD',
                         'SCULK', 'ENCHANTING_TABLE', 'COMMAND_BLOCK', 'BEACON', 'ANVIL', 'TERRACOTTA',
                         'SUNFLOWER', 'LILAC', 'ROSE_BUSH', 'PEONY', 'SHULKER_BOX', 'HEAVY_CORE', 'FERN', 'AZALEA',
                         'TNT', 'TURTLE_EGG', 'SNIFFER_EGG', 'REPEATER', 'COMPARATOR', 'PISTON',
                         'BARRIER', 'HOPPER', 'DISPENSER', 'DROPPER', 'LECTERN', 'TARGET', 'LEVER',
                         'SEA_LANTERN', 'STRUCTURE_VOID', 'CONDUIT', 'SCAFFOLDING', 'OBSERVER', 'LIGHTNING_ROD',
                         'DAYLIGHT_DETECTOR', 'HAY_BLOCK', 'TRIPWIRE_HOOK', 'NOTE_BLOCK', 'MUSHROOM_STEW',
                         'ACTIVATOR_RAIL', 'RAIL', 'SADDLE', 'MINECART', 'CARROT_ON_A_STICK', 'ELYTRA',
                         'STRUCTURE_BLOCK', 'FLINT', 'COOKED_PORKCHOP', 'PORKCHOP', 'GUNPOWDER', 'FEATHER',
                         'JIGSAW', 'RAW_IRON', 'RAW_GOLD', 'RAW_COPPER', 'POTATO', 'MAP',
                         'STICK', 'PAINTING', 'PAPER', 'BOOK', 'EGG', 'RECOVERY_COMPASS', 'COMPASS',
                         'COD', 'SALMON', 'TROPICAL_FISH', 'PUFFERFISH', 'SUGAR', 'CAKE', 'COOKIE', 'CRAFTER', 'SHEARS',
                         'BEEF', 'GHAST_TEAR', 'SPIDER_EYE', 'ROTTEN_FLESH', 'BLAZE_ROD', 'CHICKEN', 'GLOW_INK_SAC',
                         'COCOA_BEANS', 'INK_SAC', 'NETHER_BRICK', 'BRICK', 'LIGHT', 'WOLF_ARMOR',
                         'BUNDLE', 'FISHING_ROD', 'BLAZE_POWDER', 'BREWING_STAND', 'CAULDRON', 'EXPERIENCE_BOTTLE',
                         'WIND_CHARGE', 'MACE', 'ITEM_FRAME', 'GLOW_ITEM_FRAME', 'FLOWER_POT', 'CARROT', 'NETHER_STAR',
                         'FIREWORK_ROCKET', 'FIREWORK_STAR', 'RABBIT', 'TOTEM_OF_UNDYING', 'SHULKER_SHELL',
                         'MUTTON', 'LEAD', 'NAME_TAG', 'TRIDENT','NAUTILUS_SHELL', 'DISC_FRAGMENT_5',
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
cannotFindColor = []
for k in materialMappings.keys():
    try:
        colorR = specificContainsMap[k][0]
        colorG = specificContainsMap[k][1]
        colorB = specificContainsMap[k][2]
        print('\033[38;2;%d;%d;%dm%s %s\033[0m' % (
            colorR, colorG, colorB, k, materialMappings[k]))
    except Exception as e:
        if specificContainsMap[k] is None:
            cannotFindColor.append(k)
        else:
            print(k, specificContainsMap[k])
            raise e

print('satisfied/total:%d/%d' % (satisfiedCounter, len(allMaterials)))
print(notFounds)
print(cannotFindColor)

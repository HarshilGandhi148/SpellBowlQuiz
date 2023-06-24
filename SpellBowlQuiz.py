#Spell Bowl Quiz App
#Created by Harshil Gandhi in June 2023
#Includes the 2023-2024 Indiana Academic Spell Bowl Word list

#---------------------------------------------------------------------------------------------- LIST PROCESSING --------------------------------------------------------------------------------------------------

#words from list copied and pasted into sets of 100 (still needs to be cleaned)
WORD_STRING_100 = "1. a posteriori 2. a priori 3. abbacy 4. aberrant 5. abjection 6. abjectly 7. about-face 8. abrogated 9. absolutely 10. absolution 11. abstainer 12. Abu Dhabi 13. abundance 14. academician 15. acceptable 16. acclimation 17. accomplishment 18. accordance 19. accrual 20. acculturation 21. accusingly 22. accustom 23. Achilles 24. achingly 25. acoustically 26. acreage 27. activation 28. actively 29. acutely 30. ad infinitum 31. adenoid 32. Adirondack Mountains 33. adjacency 34. adjunctive 35. adjuration 36. admiralty 37. admonition 38. admonitory 39. adrenocorticosteroid 40. advance directive 41. adventuresome 42. advisedly 43. aeronautics 44. affiance 45. affidavit 46. affray 47. affront 48. aftereffect 49. agglutination 50. aggrandizement 51. aghast 52. agilely 53. agrarian 54. agreeability 55. air-condition 56. aisle 57. albeit 58. albino 59. aldermanic 60. alertly 61. alibiing 62. alkalinity 63. allegorize 64. allspice 65. alteration 66. altercate 67. alumnus 68. Amazon 69. amblyopia 70. amelioration 71. amiability 72. amnesia 73. amnesty 74. amortizing 75. ampoule 76. analgesic 77. anarchism 78. anchovy 79. anesthetize 80. Anglophile 81. Anglo-Saxon 82. animalcule 83. animalism 84. Annapolis 85. annunciation 86. answerable 87. antacid 88. antediluvian 89. antelope 90. anthropologist 91. antigen 92. antihistamine 93. antiquated 94. antiquating 95. antonym 96. Apache 97. aphoristic 98. apiarist 99. apocalyptic 100. apocrypha"
WORD_STRING_200 = "101. apostate 102. appalled 103. appeasable 104. apperceptive 105. appertain 106. applicatory 107. applique 108. appositive 109. appraisal 110. apprentice 111. apprenticed 112. approval 113. arachnid 114. arbiter 115. arborvitae 116. arbutus 117. archducal 118. Arcturus 119. ardency 120. Aristophanes 121. Aristotelian 122. armistice 123. arresting 124. arrival 125. arterial 126. articulator 127. ascorbic acid 128. ascribable 129. asparagus 130. aspect 131. aspiration 132. assay 133. assertion 134. assertive 135. assignment 136. assignor 137. associative 138. assumption 139. astonishing 140. astronaut 141. astronomer 142. asymptote 143. ataxia 144. atmospheric 145. atrocity 146. attaint 147. attar 148. attiring 149. attitude 150. attributive 151. attrition 152. audible 153. audibly 154. augmentative 155. augur 156. austerity 157. Australia 158. authorized 159. authorizing 160. automotive 161. avant-garde 162. avarice 163. aviation 164. avuncular 165. awning 166. awry 167. bacchanal 168. backgammon 169. badinage 170. baguette 171. balbriggan 172. balconies 173. ball bearing 174. ballad 175. balsam 176. bandeau 177. banh mi 178. banns 179. barbarianism 180. barbless 181. barcarole 182. bargainer 183. barred 184. basal metabolism 185. basically 186. basilar 187. bassinet 188. basso 189. bawdily 190. beadle 191. beautify 192. begrime 193. begrudge 194. Belgian 195. bellicose 196. bemire 197. beneficence 198. benison 199. benzene 200. Bermuda"
WORD_STRING_300 = "201. besmirch 202. bethel 203. Bethlehem 204. bewitchment 205. bibliomania 206. bibliophile 207. biddable 208. bight 209. billable 210. billboard 211. bimetallic 212. bimonthly 213. biographer 214. biographic 215. bird’s-eye 216. biretta 217. bishopric 218. bismuth 219. bituminous 220. bivalent 221. blarney 222. blazing 223. blazon 224. blood vessel 225. bloodcurdling 226. bloomer 227. blooming 228. blue-pencil 229. bodkin 230. bole 231. bolero 232. bookbindery 233. boondoggle 234. boorish 235. Boston 236. bottling 237. boundary 238. bower 239. bowery 240. boycotter 241. brainier 242. Braque 243. brazier 244. breakthrough 245. briary 246. bridging 247. brilliantine 248. brimful 249. briskly 250. broigne 251. brontosaurus 252. bronze 253. brotherliness 254. brotherly 255. bruising 256. bruit 257. brut 258. brute 259. buccaneer 260. Buchanan 261. bucolically 262. Budapest 263. buffoon 264. buffoonery 265. bulkier 266. bulkiness 267. bullion 268. bullock 269. buoyancy 270. buoyant 271. burglarproof 272. burglary 273. burnish 274. burnoose 275. busyness 276. buttonhole 277. buttress 278. byte 279. cabalist 280. caballero 281. cached 282. cachet 283. cadmium 284. cadre 285. Cairo 286. caisson 287. calcination 288. calibrate 289. callous 290. Calvary 291. Calvinist 292. canaille 293. candescence 294. cannonade 295. cantankerous 296. cantata 297. capable 298. capacious 299. capital 300. capitol"
WORD_STRING_400 = "301. capitulate 302. captious 303. carafe 304. caramel 305. Carborundum 306. carbuncle 307. career 308. caricature 309. carnivorous 310. carpus 311. cartography 312. castellated 313. catabolism 314. cataclysm 315. catalpa 316. catastrophe 317. catkin 318. catnap 319. causality 320. cavalry 321. cavern 322. ceded 323. cedilla 324. cellophane 325. censorship 326. centralization 327. cerebral 328. cerebrum 329. certiorari 330. certitude 331. chain-smoke 332. chameleon 333. chamois 334. chantey 335. chanticleer 336. chargé d’affaires 337. chargeable 338. chattily 339. cheerful 340. cheroot 341. chicanery 342. chickadee 343. chinchilla 344. Chinese 345. chiropractor 346. chirrup 347. chocolatier 348. Choctaw 349. christen 350. Christendom 351. chronicler 352. chummy 353. Cicero 354. circadian 355. circumlocution 356. circumnavigate 357. cistern 358. city-state 359. civet 360. clamminess 361. clarification 362. classifying 363. clearinghouse 364. cleavage 365. clinical 366. clinician 367. close-knit 368. clover 369. clownish 370. coalescent 371. coalescing 372. cobblestone 373. codicil 374. codification 375. cogency 376. cogent 377. coherent 378. cold-blooded 379. coldhearted 380. collarbone 381. collate 382. collie 383. collier 384. collusively 385. cologne 386. coloratura 387. comatose 388. comeuppance 389. comfit 390. commanding 391. commensurate 392. commissary 393. commonwealth 394. commotion 395. commutation 396. comparison 397. compensating 398. complainant 399. complicity 400. complied"
WORD_STRING_500 = "401. compost 402. composure 403. comptroller 404. compulsion 405. concealment 406. concede 407. conception 408. conciliator 409. conciliatory 410. condenser 411. conductance 412. conduction 413. conferring 414. configuration 415. confluence 416. confutation 417. congregate 418. conjecture 419. conjoin 420. connectivity 421. consanguineous 422. consequential 423. consequently 424. consistency 425. conspicuous 426. conspiracy 427. constituency 428. construed 429. contagion 430. contemptible 431. continent 432. contour 433. contraband 434. contraption 435. contrapuntal 436. contriving 437. conundrum 438. convalescence 439. conversant 440. convince 441. convincingly 442. Copernicus 443. copilot 444. cornflower 445. corporeal 446. corps 447. corpse 448. corresponding 449. corridor 450. corruption 451. corsage 452. cosmography 453. cottontail 454. cottonwood 455. counterfeit 456. countermand 457. courageous 458. couturier 459. covalent 460. covenant 461. cowling 462. craftily 463. crappie 464. crash cart 465. creaky 466. creditable 467. creditor 468. crescendo 469. crescent 470. criminality 471. criterion 472. Croix de Guerre 473. Cro-Magnon 474. croton 475. croupier 476. cruelty 477. crying 478. cryptic 479. cuddled 480. cultural 481. cum laude 482. cupola 483. curio 484. curried 485. currycomb 486. cuspid 487. cutlass 488. cutlery 489. cyclical 490. cymbal 491. cynicism 492. cynosure 493. daguerreotype 494. dahlia 495. Damascus 496. damask 497. dandified 498. Darjeeling 499. daughter-in-law 500. dauntless"
WORD_STRING_600 = "501. dazzlingly 502. de facto 503. deathbed 504. debilitate 505. debilitation 506. decalcomania 507. decalogue 508. deceive 509. decimal 510. decimate 511. declension 512. declination 513. decorum 514. decrease 515. deductible 516. deferring 517. defiance 518. definitive 519. degenerate 520. deixis 521. deliberate 522. deliberation 523. deliquescence 524. demagnetize 525. demijohn 526. demilitarization 527. demoniac 528. demurring 529. denouement 530. denounced 531. Denver 532. depiction 533. depositary 534. depressant 535. depressed 536. deranging 537. derelict 538. derrick 539. derring-do 540. desensitize 541. desert 542. desirous 543. desist 544. despondent 545. despot 546. dessert 547. desultory 548. determination 549. determine 550. detrimental 551. Detroit 552. deviation 553. Dewey 554. dewy 555. diagnostic 556. diagnostician 557. diaper 558. diaphanous 559. dichromatic 560. dietary 561. diffusive 562. dilapidated 563. dimension 564. diminish 565. disarmament 566. discern 567. discomfort 568. discommode 569. discontent 570. discourteous 571. discourtesy 572. discursive 573. discus 574. discuss 575. disfigurement 576. disfranchise 577. dishonesty 578. disjunction 579. disobedience 580. dispatch 581. dispel 582. display 583. displease 584. disqualification 585. disqualify 586. dissemination 587. dissension 588. dissociation 589. dissoluble 590. distensible 591. distortion 592. disunion 593. disunite 594. divergently 595. diverse 596. doggerel 597. dolorous 598. dolphin 599. Dominican 600. dominie"
WORD_STRING_700 = "601. dossier 602. Dostoyevsky 603. doubtless 604. draftee 605. dramatize 606. dramaturgy 607. drearily 608. dropsy 609. ducat 610. dulcimer 611. dunghill 612. Dunkirk 613. durance 614. duration 615. dynamo 616. dynamometer 617. Easterner 618. Eastertide 619. ebony 620. ebullience 621. eclectic 622. ecru 623. ecstasy 624. edema 625. Eden 626. edition 627. eeriness 628. effervescing 629. effete 630. effulgent 631. effuse 632. egotistic 633. eighty 634. Einstein 635. elapsing 636. electioneer 637. electrodynamics 638. electrolysis 639. electrotherapy 640. electrotype 641. elephantine 642. elevate 643. eliminate 644. elopement 645. eloping 646. emaciation 647. emanate 648. embarrass 649. embarrassingly 650. emblematic 651. embrocation 652. embroider 653. emergent 654. emeritus 655. emitted 656. emphasizing 657. emphatic 658. empurpled 659. enabling 660. enchain 661. enchanting 662. encouragement 663. encouraging 664. endemic 665. endemically 666. endurance 667. endure 668. engraving 669. enkindle 670. enrapture 671. entablature 672. entail 673. enthusiastic 674. enthusiastically 675. entrancing 676. entwine 677. enumerate 678. environ 679. envisage 680. epically 681. epilepsy 682. epileptic 683. epitaph 684. epithelial 685. equality 686. equilibrate 687. equivocal 688. equivocate 689. erector 690. ergo 691. errant 692. eruption 693. eruptive 694. escarole 695. escarpment 696. Esperanto 697. espionage 698. estate 699. esteem 700. etching"
WORD_STRING_800 = "701. eternal 702. ethnically 703. etymology 704. eucalyptus 705. euphemism 706. euphemistic 707. European 708. evangelical 709. evangelism 710. eventide 711. eventual 712. eviction 713. evidence 714. evolving 715. exaltation 716. examination 717. excelling 718. excelsior 719. excitation 720. excrescence 721. execrable 722. execrate 723. exemption 724. exhortation 725. exoneration 726. exorbitant 727. expatriation 728. expectancy 729. expelling 730. expiratory 731. exploratory 732. expository 733. expostulate 734. expunging 735. expurgate 736. extensor 737. extirpate 738. extradition 739. extricable 740. extricate 741. exultation 742. exurbanite 743. fabrication 744. faction 745. factious 746. faint 747. falconry 748. fall out 749. fallout 750. falsify 751. fanatical 752. fanaticism 753. fantastically 754. fantasy 755. farrier 756. farrow 757. fashionable 758. fasten 759. fathomless 760. fatigue 761. faultless 762. feasibility 763. feasible 764. fecundity 765. federal 766. feigned 767. female 768. feminine 769. fermentation 770. fermium 771. fertilize 772. fetching 773. fete 774. feverish 775. fibrous 776. fibula 777. fiduciary 778. fief 779. figuration 780. Filipino 781. filtration 782. finagle 783. Finland 784. firework 785. fixation 786. flagstone 787. flail 788. flange 789. flanged 790. flashy 791. flaxen 792. fleur-de-lis 793. Floridian 794. floridity 795. fluidity 796. fluky 797. flurry 798. flyweight 799. flywheel 800. follicle"
WORD_STRING_900 = "801. foolery 802. foolhardiness 803. forceps 804. forcible 805. forester 806. forger 807. forgery 808. formality 809. formulation 810. formulator 811. fortified 812. fossilize 813. fragile 814. fragility 815. Franciscan 816. frangibility 817. fratricide 818. fraudulence 819. Freemason 820. freemasonry 821. freer 822. frequency 823. frequent 824. friction 825. fringing 826. frippery 827. frontage 828. frowzier 829. frumpy 830. fulcrum 831. fumed 832. fumigate 833. fungicide 834. fungous 835. furnishing 836. furtively 837. fury 838. fuzziness 839. gage 840. Galahad 841. gallium 842. gallivant 843. galvanoscope 844. gamut 845. gaped 846. gargled 847. gargling 848. garret 849. garrison 850. gaslighting 851. gasometer 852. gaucherie 853. gaudier 854. gauge 855. gauntlet 856. gawkiness 857. gelatin 858. gelatinous 859. gendarme 860. generative 861. generator 862. genitive 863. genotype 864. genuflection 865. genuine 866. geometry 867. geophysicist 868. germanium 869. Germany 870. gestapo 871. gestate 872. geyser 873. ghastliness 874. gilt-edged 875. girdling 876. girlhood 877. gladiatorial 878. Glasgow 879. glasnost 880. glengarry 881. gloatingly 882. global 883. glorifying 884. glowworm 885. glucose 886. gnash 887. gobbler 888. Godspeed 889. Gomorrah 890. gooseberry 891. gooseneck 892. goshawk 893. gosling 894. governance 895. governess 896. gradual 897. grandee 898. grandeur 899. granularity 900. granulate"
WORD_STRING_1000 = "901. grasshopper 902. grazing 903. greasewood 904. greenhouse 905. greensward 906. greenwash 907. grievance 908. grieve 909. grocer 910. grosgrain 911. grossly 912. groveled 913. groveling 914. grumbling 915. guardsman 916. Guatemala 917. guiding 918. guidon 919. gustatory 920. gustily 921. gymnast 922. haberdashery 923. hackamore 924. hackberry 925. hagridden 926. Haifa 927. halfhearted 928. Halloween 929. hallucination 930. handmaiden 931. hangover 932. hanker 933. harassment 934. harmonium 935. harmonization 936. harshly 937. hartebeest 938. hatchway 939. havoc 940. hazily 941. hazing 942. healthful 943. healthier 944. heartily 945. heaving 946. hector 947. Hecuba 948. heinous 949. helminth 950. hemophiliac 951. hemorrhage 952. heptagon 953. heptagonal 954. hereafter 955. hereby 956. hermetically 957. herringbone 958. hewed 959. hibernation 960. Hibernia 961. highboy 962. hillock 963. hinterland 964. Hippocrates 965. history 966. hobbling 967. homogeneous 968. honeybee 969. horehound 970. horizon 971. horrid 972. horrified 973. hortatory 974. horticulture 975. hostility 976. housewarming 977. huddling 978. humanitarian 979. humanity 980. humiliating 981. hunchback 982. hurler 983. hurly-burly 984. husking 985. hydraulic 986. hydroid 987. hydrolysis 988. hydrous 989. hydroxide 990. hyperacid 991. hyperacidity 992. hypnotize 993. hypothesis 994. hypothesize 995. idealism 996. idiocy 997. idiom 998. idyllic 999. ileum 1000. ilex"
WORD_STRING_1100 = "1001. illimitable 1002. Illinois 1003. illusory 1004. imitable 1005. immediate 1006. immobilization 1007. immobilize 1008. immunity 1009. impalpable 1010. impeachable 1011. impenetrability 1012. imperialistic 1013. imperil 1014. imperturbable 1015. impervious 1016. implement 1017. implicate 1018. importune 1019. importuning 1020. impracticability 1021. impression 1022. improvement 1023. impulse 1024. inaccessible 1025. inaccuracy 1026. inanimate 1027. incarnate 1028. inchoately 1029. inciting 1030. incoherent 1031. incompetent 1032. incomplete 1033. inconsistency 1034. inconsolable 1035. incorporate 1036. incredulous 1037. increment 1038. incunabula 1039. indefatigability 1040. indemnity 1041. indigestion 1042. indignant 1043. indistinct 1044. indistinguishable 1045. Indonesia 1046. indulge 1047. inebriation 1048. inelasticity 1049. inelegance 1050. inescapable 1051. inestimable 1052. inexplicability 1053. infantry 1054. inferiority 1055. infernal 1056. infinitely 1057. infinitesimal 1058. inflationary 1059. informality 1060. infusible 1061. ingratiation 1062. ingratitude 1063. inherent 1064. inimitable 1065. iniquitous 1066. injustice 1067. inoculation 1068. inquisitive 1069. inquisitor 1070. insecticide 1071. insectivore 1072. insignia 1073. insignificance 1074. insolvent 1075. installation 1076. installment 1077. institution 1078. insular 1079. insurgent 1080. insuring 1081. integument 1082. intellect 1083. intensify 1084. intensity 1085. interchangeable 1086. interferon 1087. interfuse 1088. intermediary 1089. interpellate 1090. interplanetary 1091. interrogation 1092. intervene 1093. intonation 1094. intricate 1095. intrigue 1096. intuition 1097. invasion 1098. invective 1099. investigation 1100. inviolate"
WORD_STRING_1200 = "1101. invisibility 1102. involving 1103. invulnerable 1104. irascibility 1105. irascible 1106. Iroquois 1107. irrelevance 1108. irreversible 1109. isinglass 1110. isle 1111. isolationists 1112. isotropic 1113. Israel 1114. itemize 1115. iterate 1116. jabot 1117. jasmine 1118. jessamine 1119. jester 1120. Jezebel 1121. jibbing 1122. jitterbug 1123. jittery 1124. Johannesburg 1125. jubilant 1126. jubilation 1127. jujitsu 1128. juvenile 1129. Khrushchev 1130. kibitzer 1131. kilocycle 1132. kilogram 1133. kinematics 1134. kinescope 1135. Kipling 1136. kismet 1137. Knickerbocker 1138. knowledgeable 1139. knuckle 1140. labeling 1141. lackadaisical 1142. lambency 1143. lambent 1144. Lancashire 1145. Lancaster 1146. Laos 1147. largesse 1148. larghetto 1149. Latin 1150. launched 1151. launder 1152. leach 1153. leaden 1154. leech 1155. leeringly 1156. legatee 1157. legation 1158. legislator 1159. leprechaun 1160. leprosy 1161. levitate 1162. Levite 1163. libelous 1164. libretto 1165. license 1166. life expectancy 1167. lightning 1168. limy 1169. linguist 1170. liquefied 1171. liquefy 1172. literally 1173. literary 1174. litigation 1175. liveried 1176. liverwurst 1177. logarithmic function 1178. London 1179. loony 1180. loophole 1181. lotus 1182. lovely 1183. lozenge 1184. luminary 1185. luminescent 1186. lurched 1187. lustrum 1188. lymphocyte 1189. maceration 1190. MacGyver 1191. macrocosmic 1192. macron 1193. magna cum laude 1194. magneto 1195. magnification 1196. maidservant 1197. Malacca 1198. malachite 1199. maleficence 1200. malleability"
WORD_STRING_1300 = "1201. malleable 1202. manacling 1203. manage 1204. mandrel 1205. mandrill 1206. Manhattan 1207. manhole 1208. manioc 1209. manipulate 1210. manorial 1211. manumit 1212. Marco Polo 1213. Marconi 1214. maritally 1215. maritime 1216. martingale 1217. mater 1218. matins 1219. matriarch 1220. mattock 1221. mawkish 1222. maxilla 1223. meagerly 1224. mechanic 1225. mediation 1226. meditative 1227. megaphone 1228. megaton 1229. melodeon 1230. melodic 1231. memorable 1232. mendacity 1233. Mendelssohn 1234. mentholated 1235. merchantman 1236. merganser 1237. mesdames 1238. mesmerism 1239. metamorphism 1240. meteorite 1241. meteorological 1242. meticulous 1243. metonymy 1244. mezzotint 1245. Miami 1246. microorganism 1247. militating 1248. milliard 1249. milligram 1250. mimeograph 1251. mimetic 1252. mingling 1253. ministry 1254. miniver 1255. minutiae 1256. mirabile visu 1257. misanthropically 1258. misanthropist 1259. misbeliever 1260. miscibility 1261. miser 1262. miserable 1263. misinform 1264. misinformation 1265. misnomer 1266. misogamist 1267. misrepresentation 1268. misspelled 1269. mistral 1270. mistreatment 1271. mitigation 1272. mobilize 1273. moderato 1274. modernism 1275. modifying 1276. modish 1277. moisten 1278. moistly 1279. mollify 1280. mollifying 1281. monarchic 1282. monarchist 1283. moneybags 1284. moneyed 1285. monitory 1286. monkey wrench 1287. monogrammatic 1288. monopolize 1289. monsieur 1290. monsignor 1291. Montpelier 1292. moorland 1293. morbidity 1294. morning glory 1295. morocco 1296. mortally 1297. mortar 1298. Moselle 1299. motherly 1300. mother-of-pearl"
WORD_STRING_1400 = "1301. motorcyclist 1302. motorist 1303. Mount Fujiyama 1304. mourner 1305. mournful 1306. Mozart 1307. mucilage 1308. muffling 1309. mufti 1310. multicolored 1311. multifarious 1312. multitudinous 1313. muscle-bound 1314. muscular 1315. musketeer 1316. mutability 1317. myopic 1318. myriad 1319. mythological 1320. nankeen 1321. narcotic 1322. Nassau 1323. nastily 1324. nationalize 1325. Naugahyde 1326. navigable 1327. navigate 1328. nearsighted 1329. neckerchief 1330. needlepoint 1331. needless 1332. negligence 1333. neighborliness 1334. neither 1335. nervation 1336. nerveless 1337. neural 1338. neuropathy 1339. neurosis 1340. New Orleans 1341. New Zealand 1342. niche 1343. nickel 1344. nimbus 1345. Nimrod 1346. niter 1347. noisome 1348. nonacceptance 1349. nonage 1350. nonessential 1351. nonesuch 1352. nonsupport 1353. North Dakota 1354. nostalgic 1355. noteworthiness 1356. nougat 1357. nourish 1358. novocaine 1359. nowadays 1360. nudged 1361. numbly 1362. nuptial 1363. Nuremberg 1364. nutritionist 1365. oarsman 1366. oases 1367. obeying 1368. objet d’art 1369. objurgate 1370. obliteration 1371. obscurely 1372. obsession 1373. obsessive 1374. obstruct 1375. obstruction 1376. obversely 1377. obviate 1378. occlusion 1379. Oceania 1380. odious 1381. odist 1382. offensive 1383. offsetting 1384. okapi 1385. olein 1386. Omar Khayyam 1387. ombudsman 1388. omicron 1389. omnipresent 1390. omniscience 1391. onomatopoeia 1392. operatic 1393. opine 1394. opposing 1395. optimism 1396. orangeade 1397. orangutan 1398. orchestration 1399. orchid 1400. organically"
WORD_STRING_1500 = "1401. organism 1402. originate 1403. ornithology 1404. orotund 1405. orthography 1406. osmosis 1407. osmotic 1408. osteopathy 1409. ostler 1410. Ouija 1411. outre 1412. overbearing 1413. owing 1414. owlet 1415. Oxonian 1416. oxyacetylene 1417. pacification 1418. paddling 1419. paddy 1420. paillette 1421. painfully 1422. palate 1423. palatial 1424. palisade 1425. palladium 1426. palomino 1427. palpability 1428. pamphleteer 1429. panacea 1430. pantaloon 1431. papaya 1432. parabolic 1433. parachute 1434. parallax 1435. paralleled 1436. paranoiac 1437. parapet 1438. Parcheesi 1439. pariah 1440. parietal 1441. parliamentarian 1442. parquetry 1443. parricidal 1444. partaken 1445. particularity 1446. particularize 1447. parvenu 1448. passionately 1449. pasteurize 1450. pastille 1451. patchwork 1452. pathetically 1453. pathfinder 1454. patriarchy 1455. patrician 1456. patron 1457. patronage 1458. pauperism 1459. pauperize 1460. pedagogy 1461. pedometer 1462. peduncle 1463. pelisse 1464. pellagra 1465. penance 1466. Penates 1467. penning 1468. pensively 1469. pentagon 1470. peonage 1471. peony 1472. per se 1473. peradventure 1474. perceptibly 1475. perception 1476. peregrine 1477. peremptorily 1478. perforator 1479. perforce 1480. perigee 1481. perihelion 1482. periphrastic 1483. periscope 1484. perjuring 1485. permissive 1486. perplex 1487. perplexity 1488. persona non grata 1489. personable 1490. perspicacious 1491. perspicacity 1492. pertinence 1493. perverse 1494. petaled 1495. petard 1496. petrol 1497. petrolatum 1498. pewee 1499. pharmaceutical 1500. phenolic"
WORD_STRING_1600 = "1501. phenomenal 1502. phenotype 1503. Philippines 1504. Philistine 1505. phlegmatic 1506. phlox 1507. phonological 1508. photoflash 1509. photogenic 1510. piazza 1511. pica 1512. piebald 1513. piece de resistance 1514. pigeon 1515. pilchard 1516. pimento 1517. pimpernel 1518. Ping-Pong 1519. pioneer 1520. pious 1521. pirouette 1522. piscatorial 1523. pithy 1524. pitiable 1525. placability 1526. placable 1527. plagiarism 1528. plagiarist 1529. plant-based 1530. plasticity 1531. plaudit 1532. plausibility 1533. pleading 1534. pleasant 1535. plenipotentiary 1536. plenitudinous 1537. pliancy 1538. pluvial 1539. podgy 1540. podiatrist 1541. poignant 1542. poinsettia 1543. polarity 1544. polarization 1545. polish 1546. politburo 1547. pollute 1548. polygonal 1549. polytheistic 1550. popularization 1551. porpoise 1552. porridge 1553. portico 1554. portiere 1555. posing 1556. position 1557. post meridiem 1558. posturing 1559. potion 1560. prankster 1561. prating 1562. precautionary 1563. precipitant 1564. precipitate 1565. pre-Columbian 1566. preconceive 1567. predetermine 1568. predispose 1569. prefabrication 1570. preface 1571. prefigurative 1572. prelacy 1573. prelate 1574. prenatal 1575. preoccupancy 1576. preponderant 1577. Presbyterianism 1578. presbytery 1579. presentiment 1580. presently 1581. prestidigitation 1582. prestidigitator 1583. pretension 1584. pretentious 1585. prevaricator 1586. priding 1587. primitive 1588. principle 1589. printable 1590. privateer 1591. probating 1592. probation 1593. proclamation 1594. procured 1595. productive 1596. productivity 1597. proffer 1598. proficiency 1599. progenitor 1600. progressively"
WORD_STRING_1700 = "1601. prohibit 1602. prolific 1603. prolificacy 1604. propellent 1605. propeller 1606. propitiate 1607. propitiation 1608. proprietary 1609. proscription 1610. proscriptively 1611. prospective 1612. prospector 1613. protectively 1614. prototypical 1615. provable 1616. provincialism 1617. proximity 1618. prying 1619. psalm 1620. psychoanalyst 1621. psychotic 1622. ptarmigan 1623. pugilism 1624. pulpiness 1625. pumpernickel 1626. purchaser 1627. puritanism 1628. pursued 1629. pustular 1630. pygmy 1631. pylorus 1632. quadrant 1633. quadrate 1634. quaintly 1635. quarantine 1636. quatrain 1637. quavering 1638. querying 1639. questionable 1640. quick-witted 1641. quid pro quo 1642. quintuplet 1643. quondam 1644. radial 1645. radiotelephone 1646. raisin 1647. ramifying 1648. ranged 1649. rarely 1650. ratifying 1651. raucous 1652. razzle-dazzle 1653. realization 1654. reasonable 1655. rebus 1656. rebut 1657. receded 1658. receptor 1659. reciting 1660. recklessly 1661. recollection 1662. recommend 1663. reconsider 1664. recreative 1665. recriminate 1666. rectify 1667. rectilinear 1668. redaction 1669. reducible 1670. referable 1671. referee 1672. reflector 1673. reflex 1674. refrangible 1675. refutable 1676. regency 1677. regeneracy 1678. registrar 1679. regulator 1680. regulatory 1681. reincarnation 1682. rejuvenation 1683. relaxedly 1684. reliance 1685. reliquary 1686. remedial 1687. remedied 1688. remittance 1689. removing 1690. reneging 1691. renegotiate 1692. renowned 1693. reparative 1694. repartee 1695. repelling 1696. replenishment 1697. replete 1698. reprehensibility 1699. reprisal 1700. reproach"
WORD_STRING_1800 = "1701. reptilian 1702. reputably 1703. requiting 1704. rescind 1705. resentment 1706. reservation 1707. residual 1708. residuary 1709. resistless 1710. resistor 1711. resourcefully 1712. resplendent 1713. restoration 1714. resuming 1715. resumption 1716. retrace 1717. retribution 1718. retrospective 1719. returnable 1720. revenge 1721. revengeful 1722. reversal 1723. rhea 1724. rhenium 1725. rhinitis 1726. rhinoceros 1727. rialto 1728. righteousness 1729. riotous 1730. ritualistic 1731. rococo 1732. Roman numeral 1733. rondo 1734. rootstock 1735. rosier 1736. roster 1737. rotunda 1738. rotundity 1739. roundup 1740. royalist 1741. ruching 1742. ruination 1743. rumpling 1744. rumpus 1745. Russian 1746. Sabbath 1747. sabbatical 1748. sacred 1749. sacrifice 1750. saddlery 1751. Sadducee 1752. sagamore 1753. sagebrush 1754. Saipan 1755. salicylic 1756. Salome 1757. salon 1758. salute 1759. saluting 1760. sampler 1761. sanction 1762. sanctity 1763. sangfroid 1764. sanguinarily 1765. sapience 1766. sapling 1767. sarcoma 1768. sarcophagus 1769. satchel 1770. satirizing 1771. satisfaction 1772. saturnism 1773. satyr 1774. sauterne 1775. savage 1776. scabrous 1777. scampish 1778. scandal 1779. scapegrace 1780. scapula 1781. scarring 1782. scheduled 1783. scholarly 1784. scientific 1785. Scotland 1786. Scranton 1787. scrapbook 1788. scrofulous 1789. scuffling 1790. scull 1791. scuttle 1792. scuttlebutt 1793. seamstress 1794. secretory 1795. sedulous 1796. segmentation 1797. segregate 1798. seizure 1799. self-esteem 1800. self-important"
WORD_STRING_1900 = "1801. semaphore 1802. semiprecious 1803. Semite 1804. seniority 1805. sensitization 1806. sentient 1807. sentimental 1808. sentimentality 1809. sequestration 1810. sequin 1811. serially 1812. serrated 1813. servitude 1814. sesame 1815. seventeen 1816. sewerage 1817. sewing 1818. shadier 1819. shako 1820. shanghai 1821. Shangri-la 1822. sharply 1823. sharpshooter 1824. Sheba 1825. shillelagh 1826. shortcoming 1827. shortening 1828. shoveling 1829. shriek 1830. shrillness 1831. shrugging 1832. shrunken 1833. Siamese 1834. Sibelius 1835. sideboard 1836. sideburns 1837. sieve 1838. significant 1839. silicate 1840. silicon 1841. similarity 1842. simile 1843. simplified 1844. simplify 1845. sincerest 1846. sincerity 1847. singling 1848. sinusitis 1849. Sioux 1850. slacken 1851. slake 1852. sleepily 1853. slickness 1854. slothful 1855. snippier 1856. snowier 1857. sociological 1858. sogginess 1859. solemnity 1860. soliloquist 1861. solution 1862. solvable 1863. songster 1864. sonic 1865. sophist 1866. sophistic 1867. sorceress 1868. sorcery 1869. soulfully 1870. soulless 1871. Southerner 1872. spatiality 1873. spatially 1874. speciality 1875. specialization 1876. speckling 1877. speculating 1878. speculation 1879. sphinx 1880. spinal 1881. spiracular 1882. spiral 1883. spirituous 1884. splendiferous 1885. spryly 1886. spume 1887. spyglass 1888. squashiness 1889. squeezing 1890. stabilizer 1891. stagnate 1892. stagnating 1893. standby 1894. standee 1895. staring 1896. starkly 1897. statehood 1898. statistician 1899. statistics 1900. steadily"
WORD_STRING_2000 = "1901. steerage 1902. stelar 1903. stentorian 1904. stepladder 1905. sterling 1906. sternly 1907. stiffening 1908. stifle 1909. stingier 1910. stinginess 1911. stoic 1912. stoical 1913. stoichiometry 1914. stratagem 1915. streaky 1916. streamer 1917. striated 1918. stricken 1919. stringy 1920. strontium 1921. strophe 1922. strychnine 1923. stuntedness 1924. stupefaction 1925. styling 1926. suavity 1927. subjection 1928. sublimely 1929. submitting 1930. subscribing 1931. subsidization 1932. substitution 1933. subvariant 1934. subvention 1935. subversion 1936. succulence 1937. sufferable 1938. sufferance 1939. suffragist 1940. suffuse 1941. suitability 1942. sullied 1943. Sumatra 1944. summa cum laude 1945. sumptuous 1946. superfluous 1947. supernumerary 1948. supersede 1949. supervisory 1950. supplicating 1951. supplication 1952. suppositional 1953. suppress 1954. surcingle 1955. surely 1956. surly 1957. surmise 1958. surrealistic 1959. survival 1960. sustainable 1961. swallow-tailed 1962. swami 1963. swelter 1964. sycophant 1965. sylvan 1966. symptomatic 1967. syncope 1968. syndic 1969. synonymy 1970. synopses 1971. Syracuse 1972. Syria 1973. table d’hote 1974. tabulator 1975. Tallahassee 1976. tallied 1977. tamper 1978. tanager 1979. tapir 1980. tarsal 1981. taunter 1982. taxidermy 1983. taxied 1984. teasel 1985. teethe 1986. telepathy 1987. temperamental 1988. tempting 1989. tempus fugit 1990. Tennessee 1991. tepid 1992. terrace 1993. terra-cotta 1994. terseness 1995. tetanus 1996. thalamus 1997. theobromine 1998. theocracy 1999. therapeutically 2000. thermostat"
WORD_STRING_2100 = "2001. thorough 2002. threshold 2003. thriftier 2004. thrush 2005. thrusting 2006. tiller 2007. tiltable 2008. timothy 2009. tip-off 2010. titanium 2011. tithe 2012. tobacconist 2013. tolerance 2014. tom-tom 2015. toneless 2016. tongue 2017. toothsome 2018. topaz 2019. topsy-turvy 2020. torque 2021. torrid 2022. torsion 2023. toting 2024. totter 2025. tousled 2026. touter 2027. tracery 2028. traduce 2029. trajectory 2030. trammel 2031. transcription 2032. transfuse 2033. translucent 2034. transmigration 2035. transpire 2036. transplant 2037. trauma 2038. traumatic 2039. treasonous 2040. treasure 2041. tremendous 2042. tremolo 2043. tribal 2044. tricuspid 2045. trillium 2046. trilogy 2047. tripoli 2048. triune 2049. trivalent 2050. trombone 2051. trompe l’oeil 2052. troupe 2053. trouser 2054. truistic 2055. tubular 2056. tucker 2057. tumultuous 2058. turboprop 2059. turbot 2060. tutti-frutti 2061. tuxedo 2062. twitcher 2063. typhoid 2064. typhoon 2065. ubiquitous 2066. ubiquity 2067. ultimatum 2068. unbecoming 2069. unbeliever 2070. unceremonious 2071. uncertain 2072. uncommunicative 2073. undecided 2074. undefined 2075. underling 2076. undertaking 2077. undertone 2078. undulate 2079. undulation 2080. unexceptional 2081. unforeseen 2082. unforgettable 2083. unhallowed 2084. unhappiness 2085. unilateral 2086. unimpeachable 2087. univalent 2088. universal 2089. unlimited 2090. unoccupied 2091. unorganized 2092. unquestionable 2093. unruffled 2094. unruly 2095. unsightly 2096. unskilled 2097. unthinking 2098. untidy 2099. unwitting 2100. uppermost"
WORD_STRING_2200 = "2101. up-to-date 2102. usury 2103. Ute 2104. vaccinate 2105. vagrant 2106. vaguely 2107. valise 2108. vanguard 2109. vanilla 2110. variation 2111. vascular 2112. vegetation 2113. venality 2114. venial 2115. Venice 2116. venturesome 2117. venturing 2118. verdant 2119. verdict 2120. vermicelli 2121. vermicide 2122. versed 2123. versicle 2124. vesicular 2125. vesper 2126. veterinary 2127. vibrating 2128. victimize 2129. victor 2130. vigilant 2131. vigilante 2132. vinaigrette 2133. vincible 2134. violence 2135. violent 2136. virtue 2137. virtuosity 2138. visitant 2139. visitation 2140. vitiation 2141. viticulture 2142. vivify 2143. viviparous 2144. vocative 2145. vociferant 2146. volcanic 2147. voluptuous 2148. volute 2149. vox populi 2150. vulnerable 2151. vulpine 2152. waggish 2153. waggle 2154. waive 2155. wallow 2156. wapiti 2157. warble 2158. warrant 2159. warrantee 2160. washed-out 2161. wastepaper 2162. waveringly 2163. webbing 2164. Weimaraner 2165. weirdly 2166. werewolf 2167. whaling 2168. whenas 2169. whetstone 2170. whetting 2171. whippersnapper 2172. whistling 2173. whodunit 2174. wildebeest 2175. wimple 2176. wince 2177. windrow 2178. winsome 2179. withstanding 2180. wolverine 2181. workaday 2182. wormhole 2183. wormwood 2184. wounded 2185. woven 2186. wreckage 2187. writhed 2188. xenophobe 2189. xenophobia 2190. Yankee 2191. yeoman 2192. yonder 2193. Yonkers 2194. Yule log 2195. yurt 2196. zeta 2197. zeugma 2198. zoned 2199. zoning 2200. Zurich"

#these lists will contain the cleaned up version of the strings with each word being an element
word_list_100 = []
word_list_200 = []
word_list_300 = []
word_list_400 = []
word_list_500 = []
word_list_600 = []
word_list_700 = []
word_list_800 = []
word_list_900 = []
word_list_1000 = []
word_list_1100 = []
word_list_1200 = []
word_list_1300 = []
word_list_1400 = []
word_list_1500 = []
word_list_1600 = []
word_list_1700 = []
word_list_1800 = []
word_list_1900 = []
word_list_2000 = []
word_list_2100 = []
word_list_2200 = []

#cleans up a string and puts it into a list
def process_string(word_string, word_list):
    sub_start = 0
    sub = False

    for i in range(0, len(word_string)):
        if not (word_string[i].isdigit()) and not (word_string[i] == ".") and not sub and not (word_string[i] == " "):
            sub_start = i
            sub = True
        elif word_string[i].isdigit() and sub:
            word_list.append(word_string[sub_start:i-1])
            sub = False
            sub_start = 0
        else:
            continue

    if sub:
        word_list.append(word_string[sub_start:(len(word_string))])

#cleans up all the strings
process_string(WORD_STRING_100, word_list_100)
process_string(WORD_STRING_200, word_list_200)
process_string(WORD_STRING_300, word_list_300)
process_string(WORD_STRING_400, word_list_400)
process_string(WORD_STRING_500, word_list_500)
process_string(WORD_STRING_600, word_list_600)
process_string(WORD_STRING_700, word_list_700)
process_string(WORD_STRING_800, word_list_800)
process_string(WORD_STRING_900, word_list_900)
process_string(WORD_STRING_1000, word_list_1000)
process_string(WORD_STRING_1100, word_list_1100)
process_string(WORD_STRING_1200, word_list_1200)
process_string(WORD_STRING_1300, word_list_1300)
process_string(WORD_STRING_1400, word_list_1400)
process_string(WORD_STRING_1500, word_list_1500)
process_string(WORD_STRING_1600, word_list_1600)
process_string(WORD_STRING_1700, word_list_1700)
process_string(WORD_STRING_1800, word_list_1800)
process_string(WORD_STRING_1900, word_list_1900)
process_string(WORD_STRING_2000, word_list_2000)
process_string(WORD_STRING_2100, word_list_2100)
process_string(WORD_STRING_2200, word_list_2200)

#----------------------------------------------------------------------------------------------------- GUI -------------------------------------------------------------------------------------------------------
from gtts import gTTS
from io import BytesIO
import pygame
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter.font import Font
from PIL import Image, ImageTk
import random
import time

#creates the window
root = Tk()
root.title("Spelling Quiz")

#width: 1707, height: 1067 - used for adjusting to any screen
width = root.winfo_screenwidth()               
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root.resizable(True, True)
root.configure(bg="#D8620F")

#initializes all variables
score = 0
total = 0
counter = 0
current_index = 0
current_list = []
#font_scale = (((width*height)^2)/((1707*1067)^2))
font_scale = (width/1707 + height/1067)/2

DELAY = 200

pygame.init()
pygame.mixer.init()

#all functions
def set_score():
    global score
    global total
    global current_list
    global current_index
    str_score = "Score: " + str(score) + "/" + str(total)
    score_label.config(text = str_score)

def reset():
    set_score()
    text_input.delete(0, END)
    root.after(DELAY ,lambda:show_label(0))
    root.after(DELAY ,lambda:speak_word())

def reset_session():
    global score
    global total
    global current_index
    global counter
    score = 0
    total = 0
    current_index = 0
    counter = 0
    reset()

def speak_word():
    global current_list
    global current_index
    tts = gTTS(text=current_list[current_index], lang='en')
    file = BytesIO()
    tts.write_to_fp(file)
    file.seek(0)
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def set_list():
    text_input.config(state="normal")
    global current_list
    match list_dropdown.current():
        case 0:
            current_list = word_list_100 + word_list_200 + word_list_300 + word_list_400 + word_list_500 + word_list_600 + word_list_700 + word_list_800 + word_list_900 + word_list_1000 + word_list_1100 + word_list_1200 + word_list_1300 + word_list_1400 + word_list_1500 + word_list_1600 + word_list_1700 + word_list_1800 + word_list_1900 + word_list_2000 + word_list_2100 + word_list_2200
        case 1:
            current_list = word_list_100.copy()
        case 2:
            current_list = word_list_200.copy()
        case 3:
            current_list = word_list_300.copy()
        case 4:
            current_list = word_list_400.copy()
        case 5:
            current_list = word_list_500.copy()
        case 6:
            current_list = word_list_600.copy()
        case 7:
            current_list = word_list_700.copy()
        case 8:
            current_list = word_list_800.copy()
        case 9:
            current_list = word_list_900.copy()
        case 10:
            current_list = word_list_1000.copy()
        case 11:
            current_list = word_list_1100.copy()
        case 12:
            current_list = word_list_1200.copy()
        case 13:
            current_list = word_list_1300.copy()
        case 14:
            current_list = word_list_1400.copy()
        case 15:
            current_list = word_list_1500.copy()
        case 16:
            current_list = word_list_1600.copy()
        case 17:
            current_list = word_list_1700.copy()
        case 18:
            current_list = word_list_1800.copy()
        case 19:
            current_list = word_list_1900.copy()
        case 20:
            current_list = word_list_2000.copy()
        case 21:
            current_list = word_list_2100.copy()
        case 22:
            current_list = word_list_2200.copy()
        case default:
            text_input.config(state="disabled")
            print("Please select a list")

    if (randomized.get() == 1):
        random.shuffle(current_list)
    reset_session()

def increase_index():
    global current_index
    global current_list
    if current_index + 1 < len(current_list):
        current_index += 1
    else:
        current_index = 0

#{int} type: corresponds to text of label
def show_label(type):
    global current_list
    global current_index
    text = ""
    match type:
        case 0:
            text = ""
            correct_label.config(fg="black")
        case 1:
            text = "Correct!"
            correct_label.config(fg="green")
        case 2:
            text = "Incorrect"
            correct_label.config(fg="red")
        case 3:
            text = "The word is: " + current_list[current_index]
            correct_label.config(fg="black")
    correct_label.config(text=text)
    

def check_word():
    global score
    global total
    global current_index
    global current_list
    global counter
    if counter == 0:
        total += 1
    if text_input.get() == current_list[current_index]:
        increase_index()
        show_label(1)
        if counter == 0:
            score += 1
        else:
            counter = 0
    else:
        if counter == 0 or counter == 1:
            show_label(2)
            counter += 1
        elif counter == 2:
            show_label(3)
            increase_index()
            counter = 0
    reset()

#allows window resizing (not perfect)
def resize():
    global new_audio, new_logo
    scale = (((root.winfo_width()*root.winfo_height())^2)/((width*height)^2))
    
    new_logo = Image.open("Pencil.png")
    new_logo = new_logo.resize(((int(125*font_scale*scale)),(int(125*font_scale*scale))), Image.LANCZOS)
    new_logo = ImageTk.PhotoImage(new_logo)
    logo.config(image = new_logo)
    
    title.config(font = ("serif", int(50*font_scale*scale), "bold"))
    text_input.config(font = ("serif", int(40*font_scale*scale)))
    list_dropdown_title.config(font = ("serif", int(25*font_scale*scale), "bold"))
    list_dropdown.config(font = ("serif", int(20*font_scale*scale)))
    font.config(family = "serif", size = int(20*font_scale*scale))
    score_label.config(font = ("serif", int(30*font_scale*scale), "bold"))
    correct_label.config(font = ("serif", int(30*font_scale*scale), "bold"))
    
    new_audio = Image.open("Audio Icon.png")
    new_audio = new_audio.resize(((int(80*font_scale*scale)),(int(80*font_scale*scale))), Image.LANCZOS)
    new_audio = ImageTk.PhotoImage(new_audio)
    audio_button.config(image = new_audio)
    
    reset_button.config(font = ("serif", int(50*font_scale*scale), "bold"))
    random_checkbox.config(font = ("serif", int(25*font_scale*scale), "bold"))
    check_button.config(font = ("serif", int(30*font_scale*scale), "bold"))

#icon
icon = PhotoImage(file="Pencil.png")
root.iconphoto(False, icon)

#top frame
top_frame = Frame(root, bg="white")
top_frame.place(relx=0/1707, rely=0/1067, relwidth=1707/1707, relheight=225/1067)

#side frame
side_frame = Frame(root, bg="#a74c0c")
side_frame.place(relx=1007/1707, rely=225/1067, relwidth = 700/1707, relheight = 842/1067)

#logo
logo = Label(top_frame,image=icon, bg="white")
logo.place(relx=45/1707, rely=50/1067)

#title
title = Label(root, text="SPELLING QUIZ", font=("serif", 50, "bold"), bg="white", fg ="black")
title.place(relx=182.5/1707, rely=87.5/1067)

#text input
text_input = Entry(root, font=("serif", 40), bg="white", highlightthickness=7, highlightbackground="black", highlightcolor="black", state="disabled")
text_input.place(relx=153.5/1707, rely=700/1067, relwidth = 700/1707, relheight = 100/1067)

#list dropdown title
list_dropdown_title = Label(root, text="List Selection: ", font=("serif", 25, "bold"), bg="#a74c0c", fg="black")
list_dropdown_title.place(relx=1125/1707, rely=300/1067)

#list dropdown
list_values = ["All Words", "Words 1 - 100"]
for j in range(1, 22):
    list_values.append("Words " + str(j*100+1) + " - " + str((j+1)*100))
list_dropdown = Combobox(root, values=list_values, font=("serif", 20), state="readonly", justify="center")
list_dropdown.set("Select Option")
list_dropdown.place(relx=1360/1707, rely=305/1067, relwidth = 300/1707, relheight = 50/1067)
font = Font(family = "serif", size = 20)
root.option_add("*TCombobox*Listbox*Font", font)
root.option_add("*TCombobox*Listbox.Justify", "center")
list_dropdown.bind('<<ComboboxSelected>>', lambda _ : set_list())

#score
score_label = Label(root, text="Score: 0/0", font=("serif", 30, "bold"), bg = "#D8620F", fg = "black")
score_label.place(relx=160/1707, rely=500/1067)

#correct/incorrect label
correct_label = Label(root, text="", font= ("serif", 30, "bold"), bg = "#D8620F", fg = "black")
correct_label.place(relx=160/1707, rely=580/1067)

#audio button
audio_image = Image.open("Audio Icon.png")
audio_image.resize((int(30*font_scale), int(30*font_scale)))
audio_image = ImageTk.PhotoImage(audio_image)
audio_button = Button(root, image = audio_image, bg = "#D8620F", activebackground = "#D8620F", bd = 0, command=speak_word)
audio_button.place(relx=750/1707, rely=575/1067)

#reset button
reset_button = Button(root, text="Reset", font=("serif", int(50*font_scale), "bold"), activebackground = "#D8620F", bd = 5, bg="#D8620F", command=set_list)
reset_button.place(relx=1207/1707, rely=750/1067, relwidth=300/1707, relheight=150/1067)

#randomize checkbox
randomized = IntVar()
random_checkbox = Checkbutton(root, text="Randomize", variable = randomized, bg="#a74c0c", font = ("serif", 25, "bold"), command=set_list, highlightcolor="white", activebackground="#a74c0c")
random_checkbox.deselect()
random_checkbox.place(relx=1125/1707, rely=400/1067)

#check button
check_button = Button(root, text="Check", font=("serif",30,"bold"), activebackground = "#a74c0c", bd = 5, bg="#a74c0c", command=check_word)
check_button.place(relx=378.5/1707, rely=825/1067, relwidth=250/1707, relheight=100/1067)

#enter key
root.bind("<Return>",lambda _ : check_word())

#window resizing
root.bind("<Configure>",lambda _ :  resize())

root.mainloop()

   

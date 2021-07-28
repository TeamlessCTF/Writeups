#!/usr/bin/env python3
from primetime import ELEMENT_LEN, primes

def decode(n: int) -> int:
    dec = [0]*ELEMENT_LEN
    for i, p in zip(range(ELEMENT_LEN), primes()):
        while n % p == 0:
            dec[i] += 1
            n //= p
    return sum(dec[i] * 256**i for i in range(ELEMENT_LEN))

mod: int = 256**ELEMENT_LEN

gen  = 90509771177623528278123728450765328269333392303792643110399077239916164994344736121589860375271285671529226797605364543101497309674440138806809131836482062422785978252555033569381214639001123825351925601889031872596095051145346277344661388973857899956582396513572158179505306242901425473589381442908409368651067561032307751893710103112779195148257608711810190611573509373897583267680487840106153329250932242618947423761567290250787368019629760785317567599097541712676730881411606609517508740292605279246078633692474364228346845709960023044833100976852902005821462900430400498009412549822359808402943049331893629595809041306307569311438048425928155012514738274654807794363265735877196364106115731766304186838203734653487551201511787138938427009625999917117576907486219288016081065404646937100392148555613033015978726870446917743960368048194938514479101312530095399624814708253338392262129530107863900661316051568495890797873945511418695511971908653994331985447366443053329321383102280538865584667295147236809673834152216087320085819476943729609484247726527377558615879320237327632655959766404895653790543453023997480840763897519140733002552910291549418599516544593766809911806496458057701839665761031390238581642167871117046936050613980696934347913981627695521244655938149790973564725348501356706402694839883664775106567720359505784063092136746083139552254385369499885604710690405717091939792672579005018824483123239327310911888852011980058353833905615267974858666714382674587042754421351975086798056872481821855662122988651624850322200854237988511741335347851361912198610569814083108442323792477092413866074754571764458033232661334353840345586374390733024167968750000000000000000000000000000000000000000000
apub = 500357207949360011860695121815899154205449526010094454587979283923848585928632790645830299149453976090217245034593189992901761945331391001831072705847529750866803738700279912225965066678805507724715185506382939990799142229405455422041035178874211011751119398295299857806816386990092657837100900358347160719366783975929360339558498954820961285465620670002225659239889936599555456580359830295682062738334991554515900855548402512120620826749650756396521580270922365597641747429056073405053306940242427219752253635745528457603722008636075237147298943858617107939076277273399231985298341212601734800636370999484513623887390101127340743342876064866252125623244784047384124434094248088541685991462467253654297437402579588310999589250019828289348424957170149192160244201016103564578588147214864367737210883054758124265449650412379712901047384113980036061641986088569966224174765198474542155526830408621034708868718697636100198425645098483952048597971766147148562801195620760539216440235693381518250562984372199863885643755757214089633375219003612064713273736559152427459535130250092023420143477707286077709232094800239072803517436957478931071194581758588450886409637439466396963345804860757070798727515483494675801215036424531830745500453844192878776568008293800605196374630455749994012121524858660398046104081319756695361411583808985083359313858106135372136738671726749040433685890796455263432281216811093299277064687480718190942550814850814407562334926077877676598543907922236613521119009586779154611789987179126766615943929772599695669520979353761815721157999238946735681596011441649989258585110321624675217941201187909029596813349743091266836232134969764625366003476480256701372331765458959029575707117530532230865877414940866110631649448043296830423058310406934224218377145264611861381237149895001131889611829956995478830008145471859396864805534974592201372189664997613965274100537255280841341170249447407571114570047875217384488392158566315390952841556785484370880052264041078786170255986678011312984641313598302687184300188325196569072886923470341432247404566641268078569475653330045976812733466593716111751384324533020583788953027557237835067004513165882907985939149646381279609629318864389650921121923020213226228513603636456117420175850185142392993312209091757679786168841969441373117841632183687309590978239277773475240704285654614023321424952810616910104960766147996764630079269409179687500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
bpub = 16886140056354929427596567134326274485089560876286587124880756776977234171194975112435706147950799696726908760658379821703149986444584878143140068702252015934960869287878322047490841738237874007046175824327084819514960404309424024113231139223861581544723516192652636805273357007644252260334729236474638160005764882935578262087486745293103885797061462688773083837075673189527385494402886609308403934147632724023257349680752961803065635925869948563007304878787110064389481872192366584512937841048468261211375429258958036548757053991996868300235304332273530321070329379020853444464240627041844300407866738869823452918322784480833423513934929560513907874987813120398493556639406496655016703649326363315033712731233353178163811161488388839390738262151375611580388444190759888831710750624276059144292899974826212289291969860139700532775617760660718794818872911412098833789379882399598261500955720072887205985369118340511562424744684639569259883139517187974824181161950853887501387501187533776882087154686028474068751277305741248685427657830194130748307070414382936407812885971658094632673983740655241311628134690600772581373912071007373125831843767625012450700810049087602396672865730638377689910261970907167046870064759518544522056232795427162931983841754885841450494951705090997053611611069917900060383989748392235104217239203473575532102615155006722382194628347358754931623088568632887718111126185067797075616155294431574382263248465435551886356909040531366803040834139857334636132106628196713569727099358483467637513761623400457735977788527032015578721718162822785170003462615480682584982243958489401431342170655879609002009895863301679816403246730998946157219824974543751650675652958447410488528133202362655228903399639156272433490870994720909626670226251331877964832588817607911429113039240473499490028276618695486368021575737295277971954819472892265787971700525462969787279175719807716828606735008026486188322740499290581075721121149217204096567012568889510467546153859876198602143814772355379175058561482130360819063434290077131027968377991635072477044088229862441648707747330048000000000000000000
c    = 4010240541516399645321195034562461743458717219622622476493704732090859438167824966510148664351969649209110773241667692984697276501182707040128953765431706761834670787505514727554018556734879304098746873934089421121324218982247512814291351924877223043671728378891265540580997799487407053766647917779316763623094334611762868712057093611941314165202770691822529980585632976853670674565411273511833281110362770513187167914301635551991652653407362535224460872087333793483316891646632494686376076558532105013390219039843977909552469638359056046774015515596827199558260021294063686136404100077341838007398597465059993890928975576168315884904951930525706619213592769136606240625593489533975645387142828210729867767278782119009331299561834682615683259310762241323090900813481384333313188349411738492701047351562906839027181345022408682546416298832221649815297100598520446510702177236903581781476059676126464154669551252010296436679203727260122943272621547188029138551212046664928456708684569207855966732611875672446792947108786585829210484574660392141694053085701648964856278540345796111300830486730030373529236112854444770251061943299296906500878069990248133167421042557041575470018986481268826219893272218420187883811123048819805445449064826589938738021139023893746912952527027222810299329863641696021085054087718325983196914452039601872746439052469287204179047225378529312836547478630121319644513116659936348718675908460300862292582892882083915587965880575007908913533392291894019388201088744671218326443475109837687802579916256424185706643145007052009351056263884426086245516495968072790560107840332325292785270761251889294074244311879282572271185728302777909531413313220715212939865522739184866268196705707066260280696302535249923384583209822803191861890646931401654221911423162123708562219923887711419797120582685051956135283939881134091672191052692914756132753539012305415879968591647612459785998064874621862898383730813805202557191218101598089805789828614247107472592605080809008373281661279063601135101044553043016070821365079615866754551254372262660601301298818637825194579280847712938995049673216656916509188770025210827227323668492245704588870179128479645964519746861500154978473782934668650516904535768949282799428827614911842356617493958178344117941689901663879465330029616060074179381566862194995633197690056062963968575373204151012941127649306394093994121093750000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

G  = decode(gen)
AP = decode(apub)
BP = decode(bpub)
C  = decode(c)

aKey = AP * pow(G, -1, mod) % mod
bKey = BP * pow(G, -1, mod) % mod

S = G * aKey * bKey % mod
M = C * pow(S, -1, mod) % mod
print(M.to_bytes(ELEMENT_LEN, 'little'))
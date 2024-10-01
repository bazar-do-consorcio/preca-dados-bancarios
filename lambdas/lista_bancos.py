import os

bancos = [
    {
        "id": "71",
        "code": "097",
        "name": "CCC Noroeste Brasileiro",
        "ispb": "04632856",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "223",
        "code": "391",
        "name": "Cooperativa de credito rural de ibiam - sulcredi/ibiam",
        "ispb": "08240446",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "178",
        "code": "634",
        "name": "Banco Triângulo",
        "ispb": "17351180",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "1016",
        "code": "478",
        "name": "Gazincred s.a. sociedade de crédito, financiamento e investimento",
        "ispb": "11760553",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "14",
        "code": "637",
        "name": "Banco Sofisa",
        "ispb": "60889128",
        "image": "https://cdn.transfeera.com/banks/sofisa.png",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "208",
        "code": "362",
        "name": "Cielo s.a.",
        "ispb": "01027058",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "23",
        "code": "707",
        "name": "Daycoval",
        "ispb": "62232889",
        "image": "https://cdn.transfeera.com/banks/daycoval.png",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "1",
        "code": "033",
        "name": "Santander",
        "ispb": "90400888",
        "image": "https://cdn.transfeera.com/banks/santander.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "183",
        "code": "654",
        "name": "Banco Renner",
        "ispb": "92874270",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "262",
        "code": "404",
        "name": "Sumup sociedade de crédito direto s.a.",
        "ispb": "37241230",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "203",
        "code": "741",
        "name": "Banco Ribeirão Preto S.A.",
        "ispb": "00517645",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "182",
        "code": "653",
        "name": "Banco Indusval",
        "ispb": "61024352",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "184",
        "code": "712",
        "name": "Banco Ourinvest",
        "ispb": "78632767",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "132",
        "code": "218",
        "name": "Banco BS2",
        "ispb": "71027866",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "224",
        "code": "273",
        "name": "Cooperativa de crédito rural de são miguel do oeste - sulcredi/são miguel",
        "ispb": "08253539",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "227",
        "code": "364",
        "name": "Gerencianet s.a.",
        "ispb": "09089356",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "228",
        "code": "340",
        "name": "Super pagamentos e administração de meios eletrônicos s.a.",
        "ispb": "09554480",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "229",
        "code": "384",
        "name": "Global finanças sociedade de crédito ao microempreendedor e à empresa de pequeno",
        "ispb": "11165756",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "232",
        "code": "274",
        "name": "Money plus sociedade de crédito ao microempreendedor e a empresa de pequeno port",
        "ispb": "11581339",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "234",
        "code": "332",
        "name": "Acesso soluções de pagamento s.a.",
        "ispb": "13140088",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "53",
        "code": "069",
        "name": "Crefisa",
        "ispb": "61033106",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "61",
        "code": "082",
        "name": "Banco Topazio",
        "ispb": "07679404",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "204",
        "code": "290",
        "name": "Pagseguro Internet S.A",
        "ispb": "08561701",
        "image": "https://cdn.transfeera.com/banks/pag_seguro.png",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "619",
        "code": "401",
        "name": "Iugu servicos na internet s/a",
        "ispb": "15111975",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "29",
        "code": "125",
        "name": "Brasil plural",
        "ispb": "45246410",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "64",
        "code": "089",
        "name": "Cooperativa de Crédito Rural da Região da Mogiana",
        "ispb": "62109566",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "1015",
        "code": "470",
        "name": "Cdc sociedade de crédito ao microempreendedor e à empresade pequeno porte ltda.",
        "ispb": "18394228",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "237",
        "code": "396",
        "name": "Hub pagamentos s.a",
        "ispb": "13884775",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "243",
        "code": "383",
        "name": "Boletobancário.com tecnologia de pagamentos ltda.",
        "ispb": "21018182",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "244",
        "code": "324",
        "name": "Cartos sociedade de crédito direto s.a.",
        "ispb": "21332862",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "246",
        "code": "380",
        "name": "Picpay servicos s.a.",
        "ispb": "22896431",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "248",
        "code": "335",
        "name": "Banco digio s.a.",
        "ispb": "27098060",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "257",
        "code": "397",
        "name": "Listo sociedade de credito direto s.a.",
        "ispb": "34088029",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "258",
        "code": "355",
        "name": "Ótimo sociedade de crédito direto s.a.",
        "ispb": "34335592",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "275",
        "code": "281",
        "name": "Cooperativa de crédito rural coopavel",
        "ispb": "76461557",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "215",
        "code": "326",
        "name": "Parati - credito, financiamento e investimento s.a.",
        "ispb": "03311443",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "261",
        "code": "408",
        "name": "Bônuscred sociedade de crédito direto s.a.",
        "ispb": "36586946",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "9",
        "code": "041",
        "name": "Banrisul",
        "ispb": "92702067",
        "image": "https://cdn.transfeera.com/banks/banrisul.png",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "12",
        "code": "212",
        "name": "Original",
        "ispb": "92894922",
        "image": "https://cdn.transfeera.com/banks/original.jpg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "704",
        "code": "546",
        "name": "U4crypto solucoes tecnologicas e financeiras sa",
        "ispb": "30980539",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "1089",
        "code": "561",
        "name": "Pay4fun instituicao de pagamento s.a.",
        "ispb": "20757199",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "58",
        "code": "079",
        "name": "Banco Original do Agronegócio",
        "ispb": "09516419",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "13",
        "code": "260",
        "name": "Nu Pagamentos S.A.",
        "ispb": "18236120",
        "image": "https://cdn.transfeera.com/banks/nubank.png",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "934",
        "code": "407",
        "name": "Índigo investimentos distribuidora de títulos e valores mobiliários ltda.",
        "ispb": "00329598",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "272",
        "code": "365",
        "name": "Solidus s.a. corretora de cambio e valores mobiliarios",
        "ispb": "68757681",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "127",
        "code": "197",
        "name": "Stone Pagamentos",
        "ispb": "16501555",
        "image": "https://cdn.transfeera.com/banks/stone.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "294",
        "code": "534",
        "name": "Ewally tecnologia e servicos s.a.",
        "ispb": "00714671",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "37",
        "code": "016",
        "name": "Creditran",
        "ispb": "04715685",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "194",
        "code": "755",
        "name": "Bank of America Merrill Lynch",
        "ispb": "62073200",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "22",
        "code": "389",
        "name": "Mercantil do Brasil",
        "ispb": "17184037",
        "image": "https://cdn.transfeera.com/banks/mercantil.png",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "69",
        "code": "095",
        "name": "Banco Confidence de Câmbio",
        "ispb": "11703662",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "46",
        "code": "047",
        "name": "Banese",
        "ispb": "13009717",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "192",
        "code": "753",
        "name": "Novo Banco Continental",
        "ispb": "74828799",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "191",
        "code": "752",
        "name": "BNP Paribas",
        "ispb": "01522368",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "933",
        "code": "430",
        "name": "Cooperativa de credito rural seara - crediseara",
        "ispb": "00204963",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "32",
        "code": "010",
        "name": "Credicoamo",
        "ispb": "81723108",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "221",
        "code": "359",
        "name": "Zema crédito, financiamento e investimento s/a",
        "ispb": "05351887",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "986",
        "code": "462",
        "name": "Stark sociedade de crédito direto s.a.",
        "ispb": "39908427",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "44",
        "code": "037",
        "name": "Banco do Estado do Pará",
        "ispb": "04913711",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "6",
        "code": "001",
        "name": "Banco do Brasil",
        "ispb": "00000000",
        "image": "https://cdn.transfeera.com/banks/bb.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "93",
        "code": "130",
        "name": "Caruana SCFI",
        "ispb": "09313766",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "155",
        "code": "412",
        "name": "Banco Capital",
        "ispb": "15173776",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "110",
        "code": "159",
        "name": "Casa do Crédito",
        "ispb": "05442029",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "950",
        "code": "450",
        "name": "Fitbank pagamentos eletronicos s.a.",
        "ispb": "13203354",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "24",
        "code": "021",
        "name": "Banestes",
        "ispb": "28127603",
        "image": "https://cdn.transfeera.com/banks/banestes.png",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "187",
        "code": "743",
        "name": "Banco Semear",
        "ispb": "00795423",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "210",
        "code": "350",
        "name": "Cooperativa de crédito rural de pequenos agricultores e da reforma agrária do ce",
        "ispb": "01330387",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "963",
        "code": "428",
        "name": "Cred-system sociedade de crédito direto s.a.",
        "ispb": "39664698",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "26",
        "code": "422",
        "name": "Banco Safra",
        "ispb": "58160789",
        "image": "https://cdn.transfeera.com/banks/safra.png",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "96",
        "code": "133",
        "name": "Confederação Nac das CCC SOL",
        "ispb": "10398952",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "241",
        "code": "377",
        "name": "Bms sociedade de crédito direto s.a.",
        "ispb": "17826860",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "207",
        "code": "330",
        "name": "Banco bari de investimentos e financiamentos s.a.",
        "ispb": "00556603",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "233",
        "code": "276",
        "name": "Senff s.a. - crédito, financiamento e investimento",
        "ispb": "11970623",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "145",
        "code": "269",
        "name": "HSBC Banco de Investimento",
        "ispb": "53518684",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "209",
        "code": "322",
        "name": "Cooperativa de crédito rural de abelardo luz - sulcredi/crediluz",
        "ispb": "01073966",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "105",
        "code": "144",
        "name": "Bexs",
        "ispb": "13059145",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "1001",
        "code": "529",
        "name": "Pinbank brasil - pagamentos inteligentes s.a.",
        "ispb": "17079937",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "225",
        "code": "368",
        "name": "Banco csf s.a.",
        "ispb": "08357240",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "966",
        "code": "444",
        "name": "Trinus sociedade de crédito direto s.a.",
        "ispb": "40654622",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "5",
        "code": "341",
        "name": "Itaú",
        "ispb": "60701190",
        "image": "https://cdn.transfeera.com/banks/itau.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "1002",
        "code": "550",
        "name": "Beetellerpay instituicao de pagamento ltda",
        "ispb": "32074986",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "85",
        "code": "119",
        "name": "Banco Western Union",
        "ispb": "13720915",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "119",
        "code": "183",
        "name": "Socred SCM",
        "ispb": "09210106",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "4",
        "code": "237",
        "name": "Bradesco",
        "ispb": "60746948",
        "image": "https://cdn.transfeera.com/banks/bradesco.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "1209",
        "code": "594",
        "name": "Embracred s/a sociedade de crédito direto",
        "ispb": "48703388",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "28",
        "code": "655",
        "name": "Banco Votorantim S.A.",
        "ispb": "59588111",
        "image": "https://cdn.transfeera.com/banks/votorantin.png",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "245",
        "code": "310",
        "name": "Vortx distribuidora de titulos e valores mobiliarios ltda.",
        "ispb": "22610500",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "937",
        "code": "425",
        "name": "Socinal s.a. - crédito, financiamento e investimento",
        "ispb": "03881423",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "115",
        "code": "174",
        "name": "Pernambucanas Financiadora",
        "ispb": "43180355",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "168",
        "code": "600",
        "name": "Banco Luso Brasileiro",
        "ispb": "59118133",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "230",
        "code": "088",
        "name": "Banco randon s.a.",
        "ispb": "11476673",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "16",
        "code": "745",
        "name": "Citibank",
        "ispb": "33479023",
        "image": "https://cdn.transfeera.com/banks/citibank.png",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "952",
        "code": "427",
        "name": "Cooperativa de credito dos servidores da universidade federal do espirito santo",
        "ispb": "27302181",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "19",
        "code": "136",
        "name": "Unicred",
        "ispb": "00315557",
        "image": "https://cdn.transfeera.com/banks/unicred.png",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "7",
        "code": "756",
        "name": "Sicoob",
        "ispb": "02038232",
        "image": "https://cdn.transfeera.com/banks/sicoob.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "3",
        "code": "104",
        "name": "Caixa Econômica",
        "ispb": "00360305",
        "image": "https://cdn.transfeera.com/banks/caixa.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "615",
        "code": "509",
        "name": "Celcoin instituicao de pagamento s.a.",
        "ispb": "13935893",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "962",
        "code": "421",
        "name": "Lar cooperativa de crédito - lar credi",
        "ispb": "39343350",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "34",
        "code": "012",
        "name": "Banco Inbursa",
        "ispb": "04866275",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "944",
        "code": "312",
        "name": "Hscm - sociedade de crédito ao microempreendedor e à empresa de pequeno porte lt",
        "ispb": "07693858",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "30",
        "code": "003",
        "name": "Banco da Amazônia",
        "ispb": "04902979",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "219",
        "code": "382",
        "name": "Fidúcia sociedade de crédito ao microempreendedor e à empresa de pequeno porte l",
        "ispb": "04307598",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "1003",
        "code": "451",
        "name": "J17 - sociedade de crédito direto s/a",
        "ispb": "40475846",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "985",
        "code": "439",
        "name": "Id corretora de títulos e valores mobiliários s.a.",
        "ispb": "16695922",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "956",
        "code": "402",
        "name": "Cobuccio sociedade de crédito direto s.a.",
        "ispb": "36947229",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "27",
        "code": "254",
        "name": "Banco Parana",
        "ispb": "14388334",
        "image": "https://cdn.transfeera.com/banks/parana-banco.png",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "129",
        "code": "208",
        "name": "Banco BTG Pactual",
        "ispb": "30306294",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "72",
        "code": "098",
        "name": "Credialiança",
        "ispb": "78157146",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "941",
        "code": "410",
        "name": "Planner sociedade de crédito ao microempreendedor s.a.",
        "ispb": "05684234",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "138",
        "code": "246",
        "name": "Banco ABC Brasil",
        "ispb": "28195667",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "960",
        "code": "419",
        "name": "Numbrs sociedade de crédito direto s.a.",
        "ispb": "38129006",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "1026",
        "code": "511",
        "name": "Magnum sociedade de crédito direto s.a.",
        "ispb": "44683140",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "172",
        "code": "612",
        "name": "Banco Guanabara",
        "ispb": "31880826",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "1051",
        "code": "526",
        "name": "Monetarie sociedade de crédito direto s.a.",
        "ispb": "46026562",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "169",
        "code": "604",
        "name": "Banco Industrial",
        "ispb": "31895683",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "254",
        "code": "329",
        "name": "Qi sociedade de crédito direto s.a.",
        "ispb": "32402502",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "63",
        "code": "084",
        "name": "Uniprime do Norte do Paraná",
        "ispb": "02398976",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "1065",
        "code": "537",
        "name": "Microcash sociedade de crédito ao microempreendedor e à empresa de pequeno porte",
        "ispb": "45756448",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "1064",
        "code": "528",
        "name": "Reag distribuidora de títulos e valores mobiliários s.a.",
        "ispb": "34829992",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "260",
        "code": "373",
        "name": "Up.p sociedade de empréstimo entre pessoas s.a.",
        "ispb": "35977097",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "256",
        "code": "348",
        "name": "Banco xp s.a.",
        "ispb": "33264668",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "961",
        "code": "435",
        "name": "Delcred sociedade de crédito direto s.a.",
        "ispb": "38224857",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "73",
        "code": "099",
        "name": "Uniprime Central",
        "ispb": "03046391",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "1004",
        "code": "460",
        "name": "Unavanti sociedade de crédito direto s/a",
        "ispb": "42047025",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "173",
        "code": "613",
        "name": "Omni Banco",
        "ispb": "60850229",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "965",
        "code": "452",
        "name": "Credifit sociedade de crédito direto s.a.",
        "ispb": "39676772",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "220",
        "code": "299",
        "name": "Sorocred   crédito, financiamento e investimento s.a.",
        "ispb": "04814563",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "959",
        "code": "406",
        "name": "Accredito - sociedade de crédito direto s.a.",
        "ispb": "37715993",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "25",
        "code": "077",
        "name": "Banco Inter",
        "ispb": "00416968",
        "image": "https://cdn.transfeera.com/banks/inter.png",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "1023",
        "code": "586",
        "name": "01 pagamentos e negocios ltda",
        "ispb": "35810871",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "642",
        "code": "536",
        "name": "Neon pagamentos s.a.",
        "ispb": "20855875",
        "image": "https://cdn.transfeera.com/banks/neon.png",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "11",
        "code": "085",
        "name": "Cooperativa Central de Crédito Urbano",
        "ispb": "05463212",
        "image": "https://cdn.transfeera.com/banks/cecred.png",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "629",
        "code": "542",
        "name": "Cloud walk meios de pagamentos e servicos ltda",
        "ispb": "18189547",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "996",
        "code": "465",
        "name": "Capital consig sociedade de crédito direto s.a.",
        "ispb": "40083667",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "134",
        "code": "224",
        "name": "Banco Fibra",
        "ispb": "58616418",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "21",
        "code": "121",
        "name": "Agiplan",
        "ispb": "10664513",
        "image": "https://cdn.transfeera.com/banks/agiplan.png",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "947",
        "code": "358",
        "name": "Midway s.a. - crédito, financiamento e investimento",
        "ispb": "09464032",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "174",
        "code": "623",
        "name": "Banco Pan",
        "ispb": "59285411",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "148",
        "code": "318",
        "name": "Banco BMG",
        "ispb": "61186680",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "10",
        "code": "070",
        "name": "Banco de Brasília - BRB",
        "ispb": "00000208",
        "image": "https://cdn.transfeera.com/banks/brb.png",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "8",
        "code": "748",
        "name": "Sicredi",
        "ispb": "01181521",
        "image": "https://cdn.transfeera.com/banks/sicredi.jpg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "20",
        "code": "004",
        "name": "Banco do Nordeste",
        "ispb": "07237373",
        "image": "https://cdn.transfeera.com/banks/banco-do-nordeste.png",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "263",
        "code": "403",
        "name": "Cora sociedade de crédito direto s.a.",
        "ispb": "37880206",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "200",
        "code": "336",
        "name": "C6 Bank",
        "ispb": "31872495",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "130",
        "code": "213",
        "name": "Banco Arbi",
        "ispb": "54403563",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "1027",
        "code": "481",
        "name": "Superlógica sociedade de crédito direto s.a.",
        "ispb": "43599047",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "70",
        "code": "096",
        "name": "Banco BM&FBovespa",
        "ispb": "00997185",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "212",
        "code": "378",
        "name": "Bbc leasing s.a. - arrendamento mercantil",
        "ispb": "01852137",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "177",
        "code": "633",
        "name": "Banco Rendimento",
        "ispb": "68900810",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "936",
        "code": "413",
        "name": "Banco bv s.a.",
        "ispb": "01858774",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "198",
        "code": "280",
        "name": "Avista S.A. Crédito, Financiamento e Investimento",
        "ispb": "23862762",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "197",
        "code": "301",
        "name": "BPP Instituição de Pagamento S.A.",
        "ispb": "13370835",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "991",
        "code": "461",
        "name": "Asaas gestão financeira instituição de pagamento s.a.",
        "ispb": "19540550",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "170",
        "code": "610",
        "name": "Banco VR",
        "ispb": "78626983",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "196",
        "code": "323",
        "name": "Mercado Pago",
        "ispb": "10573521",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "137",
        "code": "243",
        "name": "Banco Máxima",
        "ispb": "33923798",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "176",
        "code": "630",
        "name": "Banco Intercap",
        "ispb": "58497702",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "195",
        "code": "757",
        "name": "Banco Keb Hana",
        "ispb": "02318507",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "41",
        "code": "025",
        "name": "Banco Alfa",
        "ispb": "03323840",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "152",
        "code": "376",
        "name": "Banco JP Morgan",
        "ispb": "33172537",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "DIRETO"
    },
    {
        "id": "1040",
        "code": "510",
        "name": "Ffcred sociedade de crédito direto s.a..",
        "ispb": "39738065",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "INDIRETO"
    },
    {
        "id": "1029",
        "code": "597",
        "name": "Issuer administradora de cartoes ltda.",
        "ispb": "34747388",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "INDIRETO"
    },
    {
        "id": "1049",
        "code": "590",
        "name": "Repasses financeiros e solucoes tecnologicas instituicao de pagamento s.a.",
        "ispb": "40473435",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "INDIRETO"
    },
    {
        "id": "990",
        "code": "457",
        "name": "Platacred sociedade de crédito direto s.a.",
        "ispb": "39587424",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "INDIRETO"
    },
    {
        "id": "939",
        "code": "400",
        "name": "Cooperativa de crédito, poupança e serviços financeiros do centro oeste - credit",
        "ispb": "05491616",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "INDIRETO"
    },
    {
        "id": "199",
        "code": "279",
        "name": "CCR de Primavera do Leste",
        "ispb": "26563270",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "INDIRETO"
    },
    {
        "id": "222",
        "code": "286",
        "name": "Cooperativa de crédito rural de ouro   sulcredi/ouro",
        "ispb": "07853842",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "INDIRETO"
    },
    {
        "id": "249",
        "code": "349",
        "name": "Al5 s.a. crédito, financiamento e investimento",
        "ispb": "27214112",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "INDIRETO"
    },
    {
        "id": "634",
        "code": "595",
        "name": "Zoop tecnologia e meios de pagamento s.a.",
        "ispb": "19468242",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "INDIRETO"
    },
    {
        "id": "648",
        "code": "560",
        "name": "Mag pagamentos ltda",
        "ispb": "21995256",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "INDIRETO"
    },
    {
        "id": "656",
        "code": "566",
        "name": "Flagship instituicao de pagamentos ltda",
        "ispb": "23114447",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "INDIRETO"
    },
    {
        "id": "669",
        "code": "651",
        "name": "Roadpass payments & urban mobility ltda",
        "ispb": "25104230",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "INDIRETO"
    },
    {
        "id": "709",
        "code": "552",
        "name": "Madeira administradora de cartoes s/a",
        "ispb": "32192325",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "INDIRETO"
    },
    {
        "id": "932",
        "code": "593",
        "name": "Transfeera Pagamentos S.A.",
        "ispb": "27084098",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "INDIRETO"
    },
    {
        "id": "1151",
        "code": "520",
        "name": "SOMAPAY SOCIEDADE DE CREDITO DIRETO S.A.",
        "ispb": "44705774",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "INDIRETO"
    },
    {
        "id": "1059",
        "code": "523",
        "name": "Hr digital - sociedade de crédito direto s/a",
        "ispb": "44292580",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "INDIRETO"
    },
    {
        "id": "1205",
        "code": "547",
        "name": "Bnk digital sociedade de crédito direto s.a.",
        "ispb": "45331622",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": "INDIRETO"
    },
    {
        "id": "994",
        "code": "443",
        "name": "Credihome sociedade de crédito direto s.a.",
        "ispb": "39416705",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "995",
        "code": "454",
        "name": "Mérito distribuidora de títulos e valores mobiliários ltda.",
        "ispb": "41592532",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1013",
        "code": "385",
        "name": "Cooperativa de economia e credito mutuo dos trabalhadores portuarios da grande v",
        "ispb": "03844699",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1014",
        "code": "469",
        "name": "Lecca distribuidora de titulos e valores mobiliarios ltda",
        "ispb": "07138049",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "60",
        "code": "081",
        "name": "BBN",
        "ispb": "10264663",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "128",
        "code": "204",
        "name": "Banco Bradesco Cartões",
        "ispb": None,
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1018",
        "code": "471",
        "name": "Cooperativa de economia e credito mutuo dos servidores publicos de pinhão - cres",
        "ispb": "04831810",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1019",
        "code": "484",
        "name": "Maf distribuidora de títulos e valores mobiliários s.a.",
        "ispb": "36864992",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1020",
        "code": "506",
        "name": "Rji corretora de titulos e valores mobiliarios ltda",
        "ispb": "42066258",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1021",
        "code": "512",
        "name": "Captalys distribuidora de títulos e valores mobiliários ltda.",
        "ispb": "36266751",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1010",
        "code": "468",
        "name": "Portoseg s.a. - credito, financiamento e investimento",
        "ispb": "04862600",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "42",
        "code": "029",
        "name": "Banco Itaú Consignado",
        "ispb": "33885724",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "935",
        "code": "423",
        "name": "Coluna s/a distribuidora de titulos e valores mobiliários",
        "ispb": "00460065",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "940",
        "code": "429",
        "name": "Crediare s.a. - crédito, financiamento e investimento",
        "ispb": "05676026",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "942",
        "code": "328",
        "name": "Cooperativa de economia e crédito mútuo dos fabricantes de calçados de sapiranga",
        "ispb": "05841967",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "943",
        "code": "458",
        "name": "Hedge investments distribuidora de títulos e valores mobiliários ltda.",
        "ispb": "07253654",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "945",
        "code": "195",
        "name": "Valor sociedade de crédito direto s.a.",
        "ispb": "07799277",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "946",
        "code": "395",
        "name": "F.d'gold - distribuidora de títulos e valores mobiliários ltda.",
        "ispb": "08673569",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "948",
        "code": "426",
        "name": "Biorc financeira - crédito, financiamento e investimento s.a.",
        "ispb": "11285104",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "949",
        "code": "447",
        "name": "Mirae asset wealth management (brazil) corretora de câmbio, títulos e valores mo",
        "ispb": "12392983",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "951",
        "code": "416",
        "name": "Lamara sociedade de crédito direto s.a.",
        "ispb": "19324634",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "999",
        "code": "467",
        "name": "Master s/a corretora de câmbio, títulos e valores mobiliários",
        "ispb": "33886862",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1025",
        "code": "508",
        "name": "Avenue securities distribuidora de títulos e valores mobiliários ltda.",
        "ispb": "61384004",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "84",
        "code": "118",
        "name": "Standard Chartered",
        "ispb": None,
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1030",
        "code": "475",
        "name": "Banco yamaha motor do brasil s.a.",
        "ispb": "10371492",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1035",
        "code": "482",
        "name": "Sbcash sociedade de crédito direto s.a.",
        "ispb": "42259084",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "185",
        "code": "719",
        "name": "Banif",
        "ispb": None,
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1038",
        "code": "516",
        "name": "Fc financeira s.a. - crédito, financiamento e investimento",
        "ispb": "36583700",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1042",
        "code": "525",
        "name": "Intercam corretora de câmbio ltda.",
        "ispb": "34265629",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "98",
        "code": "135",
        "name": "Gradual",
        "ispb": None,
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "99",
        "code": "137",
        "name": "Multimoney",
        "ispb": None,
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1046",
        "code": "519",
        "name": "Lions trust distribuidora de títulos e valores mobiliários ltda.",
        "ispb": "40768766",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1047",
        "code": "507",
        "name": "Gerencianet s.a. - crédito, financiamento e investimento",
        "ispb": "37229413",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1054",
        "code": "521",
        "name": "Peak sociedade de empréstimo entre pessoas s.a.",
        "ispb": "44019481",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1056",
        "code": "518",
        "name": "Mercado crédito sociedade de crédito, financiamento e investimento s.a.",
        "ispb": "37679449",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "113",
        "code": "172",
        "name": "Albatross",
        "ispb": None,
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "118",
        "code": "182",
        "name": "Dacasa Financeira",
        "ispb": None,
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "87",
        "code": "122",
        "name": "Banco Bradesco BERJ",
        "ispb": "33147315",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "992",
        "code": "459",
        "name": "Cooperativa de crédito mútuo de servidores públicos do estado de são paulo - cre",
        "ispb": "04546162",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1000",
        "code": "463",
        "name": "Azumi distribuidora de títulos e valores mobiliários ltda.",
        "ispb": "40434681",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "15",
        "code": "735",
        "name": "neon",
        "ispb": None,
        "image": "https://cdn.transfeera.com/banks/neon.png",
        "spi_participant_type": None
    },
    {
        "id": "1043",
        "code": "455",
        "name": "Fênix distribuidora de títulos e valores mobiliários ltda.",
        "ispb": "38429045",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1057",
        "code": "527",
        "name": "Aticca - sociedade de crédito direto s.a.",
        "ispb": "44478623",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "938",
        "code": "411",
        "name": "Via certa financiadora s.a. - crédito, financiamento e investimentos",
        "ispb": "05192316",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "953",
        "code": "386",
        "name": "Nu financeira s.a. - sociedade de crédito, financiamento e investimento",
        "ispb": "30680829",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "954",
        "code": "398",
        "name": "Ideal corretora de títulos e valores mobiliários s.a.",
        "ispb": "31749596",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "955",
        "code": "445",
        "name": "Plantae s.a. - crédito, financiamento e investimento",
        "ispb": "35551187",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "957",
        "code": "418",
        "name": "Zipdin soluções digitais sociedade de crédito direto s/a",
        "ispb": "37414009",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "958",
        "code": "414",
        "name": "Work sociedade de crédito direto s.a.",
        "ispb": "37526080",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "121",
        "code": "188",
        "name": "Ativa Investimentos",
        "ispb": "33775974",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "206",
        "code": "272",
        "name": "Agk corretora de cambio s.a.",
        "ispb": "00250699",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "211",
        "code": "379",
        "name": "Cooperforte - cooperativa de economia e crédito mútuo dos funcionários de instit",
        "ispb": "01658426",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "213",
        "code": "360",
        "name": "Trinus capital distribuidora de títulos e valores mobiliários s.a.",
        "ispb": "02276653",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "214",
        "code": "387",
        "name": "Banco toyota do brasil s.a.",
        "ispb": "03215790",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "216",
        "code": "315",
        "name": "Pi distribuidora de títulos e valores mobiliários s.a.",
        "ispb": "03502968",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "217",
        "code": "307",
        "name": "Terra investimentos distribuidora de títulos e valores mobiliários ltda.",
        "ispb": "03751794",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "218",
        "code": "296",
        "name": "Vision s.a. corretora de cambio",
        "ispb": "04062902",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "964",
        "code": "448",
        "name": "Hemera distribuidora de títulos e valores mobiliários ltda.",
        "ispb": "39669186",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "226",
        "code": "259",
        "name": "Moneycorp banco de câmbio s.a.",
        "ispb": "08609934",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "967",
        "code": "433",
        "name": "Br-capital distribuidora de títulos e valores mobiliários s.a.",
        "ispb": "44077014",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "968",
        "code": "438",
        "name": "Planner trustee distribuidora de títulos e valores mobiliários ltda.",
        "ispb": "67030395",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "969",
        "code": "311",
        "name": "Dourada corretora de câmbio ltda.",
        "ispb": "76641497",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "231",
        "code": "319",
        "name": "Om distribuidora de títulos e valores mobiliários ltda",
        "ispb": "11495073",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "970",
        "code": "720",
        "name": "Banco rnx s.a.",
        "ispb": "80271455",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "971",
        "code": "440",
        "name": "Cooperativa de economia e crédito mútuo brf - credibrf",
        "ispb": "82096447",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "235",
        "code": "325",
        "name": "Órama distribuidora de títulos e valores mobiliários s.a.",
        "ispb": "13293225",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "236",
        "code": "331",
        "name": "Fram capital distribuidora de títulos e valores mobiliários s.a.",
        "ispb": "13673855",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "972",
        "code": "442",
        "name": "Magnetis - distribuidora de títulos e valores mobiliários ltda",
        "ispb": "87963450",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "238",
        "code": "309",
        "name": "Cambionet corretora de câmbio ltda.",
        "ispb": "14190547",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "239",
        "code": "313",
        "name": "Amazônia corretora de câmbio ltda.",
        "ispb": "16927221",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "240",
        "code": "298",
        "name": "Vip's corretora de câmbio ltda.",
        "ispb": "17772370",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "242",
        "code": "321",
        "name": "Crefaz sociedade de crédito ao microempreendedor e a empresa de pequeno porte lt",
        "ispb": "18188384",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "247",
        "code": "343",
        "name": "Ffa sociedade de crédito ao microempreendedor e à empresa de pequeno porte ltda.",
        "ispb": "24537861",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1044",
        "code": "513",
        "name": "Atf credit sociedade de crédito direto s.a.",
        "ispb": "44728700",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1058",
        "code": "535",
        "name": "Marú sociedade de crédito direto s.a.",
        "ispb": "39519944",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "250",
        "code": "374",
        "name": "Realize crédito, financiamento e investimento s.a.",
        "ispb": "27351731",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1061",
        "code": "334",
        "name": "Banco besa s.a.",
        "ispb": "15124464",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "164",
        "code": "494",
        "name": "BROU",
        "ispb": None,
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "251",
        "code": "278",
        "name": "Genial investimentos corretora de valores mobiliários s.a.",
        "ispb": "27652684",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "158",
        "code": "473",
        "name": "Banco Caixa Geral",
        "ispb": "33466988",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "56",
        "code": "076",
        "name": "Banco KDB",
        "ispb": "07656500",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "252",
        "code": "292",
        "name": "Bs2 distribuidora de títulos e valores mobiliários s.a.",
        "ispb": "28650236",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "253",
        "code": "352",
        "name": "Toro corretora de títulos e valores mobiliários ltda",
        "ispb": "29162769",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "259",
        "code": "367",
        "name": "Vitreo distribuidora de títulos e valores mobiliários s.a.",
        "ispb": "34711571",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "179",
        "code": "641",
        "name": "Banco Alvorada",
        "ispb": None,
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "277",
        "code": "371",
        "name": "Warren corretora de valores mobiliários e câmbio ltda.",
        "ispb": "92875780",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1062",
        "code": "524",
        "name": "Wnt capital distribuidora de títulos e valores mobiliários s.a.",
        "ispb": "45854066",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1066",
        "code": "541",
        "name": "Fundo garantidor de creditos - fgc",
        "ispb": "00954288",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1067",
        "code": "530",
        "name": "Ser finance sociedade de crédito direto s.a.",
        "ispb": "47873449",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1068",
        "code": "141",
        "name": "Banco master de investimento s.a.",
        "ispb": "09526594",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1069",
        "code": "522",
        "name": "Red sociedade de crédito direto s.a.",
        "ispb": "47593544",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1071",
        "code": "532",
        "name": "Eagle sociedade de crédito direto s.a.",
        "ispb": "45745537",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1072",
        "code": "539",
        "name": "Santinvest s.a. - credito, financiamento e investimentos",
        "ispb": "00122327",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "65",
        "code": "091",
        "name": "Unicred",
        "ispb": "01634601",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "264",
        "code": "306",
        "name": "Portopar distribuidora de titulos e valores mobiliarios ltda.",
        "ispb": "40303299",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "265",
        "code": "354",
        "name": "Necton investimentos  s.a. corretora de valores mobiliários e commodities",
        "ispb": "52904364",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "266",
        "code": "393",
        "name": "Banco volkswagen s.a.",
        "ispb": "59109165",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "267",
        "code": "390",
        "name": "Banco gm s.a.",
        "ispb": "59274605",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "268",
        "code": "381",
        "name": "Banco mercedes-benz do brasil s.a.",
        "ispb": "60814191",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "269",
        "code": "270",
        "name": "Sagitur corretora de câmbio ltda.",
        "ispb": "61444949",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "270",
        "code": "288",
        "name": "Carol distribuidora de titulos e valores mobiliarios ltda.",
        "ispb": "62237649",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "271",
        "code": "363",
        "name": "Singulare corretora de títulos e valores mobiliários s.a.",
        "ispb": "62285390",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "273",
        "code": "293",
        "name": "Lastro rdv distribuidora de títulos e valores mobiliários ltda.",
        "ispb": "71590442",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "274",
        "code": "285",
        "name": "Frente corretora de câmbio ltda.",
        "ispb": "71677850",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "52",
        "code": "066",
        "name": "Banco Morgan Stanley",
        "ispb": "02801938",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "276",
        "code": "283",
        "name": "Rb capital investimentos distribuidora de títulos e valores mobiliários limitada",
        "ispb": "89960090",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "278",
        "code": "289",
        "name": "Decyseo corretora de cambio ltda.",
        "ispb": "94968518",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "36",
        "code": "015",
        "name": "UBS Brasil",
        "ispb": "02819125",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "48",
        "code": "062",
        "name": "Hipercard",
        "ispb": "03012230",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "54",
        "code": "074",
        "name": "Banco Safra",
        "ispb": "03017677",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "55",
        "code": "075",
        "name": "ABN Amro",
        "ispb": "03532415",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "45",
        "code": "040",
        "name": "Banco Cargill",
        "ispb": "03609817",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "50",
        "code": "064",
        "name": "Goldman Sachs",
        "ispb": "04332281",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "47",
        "code": "060",
        "name": "Confidence Câmbio",
        "ispb": "04913129",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "43",
        "code": "036",
        "name": "Banco Bradesco BBI",
        "ispb": "06271464",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "35",
        "code": "014",
        "name": "Natixis Brasil",
        "ispb": "09274232",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "62",
        "code": "083",
        "name": "Banco da China",
        "ispb": "10690848",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "40",
        "code": "024",
        "name": "Banco Bandepe",
        "ispb": "10866788",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "68",
        "code": "094",
        "name": "Banco Finaxis",
        "ispb": "11758741",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "66",
        "code": "092",
        "name": "BRK CFI",
        "ispb": "12865507",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "126",
        "code": "196",
        "name": "Fair",
        "ispb": "32648370",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "31",
        "code": "007",
        "name": "BNDES",
        "ispb": "33657248",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "57",
        "code": "078",
        "name": "Haitong",
        "ispb": "34111187",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "38",
        "code": "017",
        "name": "BNY Mellon Banco",
        "ispb": "42272526",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "51",
        "code": "065",
        "name": "AndBank",
        "ispb": "48795256",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "39",
        "code": "018",
        "name": "Banco Tricury",
        "ispb": "57839805",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "33",
        "code": "011",
        "name": "Credit Suisse Hedging-Griffo",
        "ispb": "61809182",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "75",
        "code": "101",
        "name": "Renascença DTVM",
        "ispb": "62287735",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "59",
        "code": "080",
        "name": "B&T CC",
        "ispb": "73622748",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "74",
        "code": "100",
        "name": "Planner",
        "ispb": "00806535",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "117",
        "code": "180",
        "name": "CM Capital Markets CCTVM",
        "ispb": "02685483",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "49",
        "code": "063",
        "name": "Banco Bradescard",
        "ispb": "04184779",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "89",
        "code": "126",
        "name": "BR Partners",
        "ispb": "13220493",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "67",
        "code": "093",
        "name": "Pólocred",
        "ispb": "07945233",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "189",
        "code": "747",
        "name": "Rabobank",
        "ispb": "01023570",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "79",
        "code": "108",
        "name": "PortoCred",
        "ispb": "01800019",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "76",
        "code": "102",
        "name": "XP Investimentos",
        "ispb": "02332886",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "104",
        "code": "143",
        "name": "Treviso",
        "ispb": "02992317",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "123",
        "code": "190",
        "name": "Servicoop",
        "ispb": "03973814",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "124",
        "code": "191",
        "name": "Nova Futura CTVM",
        "ispb": "04257795",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "82",
        "code": "114",
        "name": "CECOOP",
        "ispb": "05790149",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "122",
        "code": "189",
        "name": "HS Financeira",
        "ispb": "07512441",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "77",
        "code": "105",
        "name": "Lecca CFI",
        "ispb": "07652226",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "109",
        "code": "157",
        "name": "ICAP",
        "ispb": "09105360",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "90",
        "code": "127",
        "name": "Codepe CVC",
        "ispb": "09512542",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "100",
        "code": "138",
        "name": "Get Money",
        "ispb": "10853017",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "114",
        "code": "173",
        "name": "BRL Trust",
        "ispb": "13486793",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "78",
        "code": "107",
        "name": "Banco Bocom BBM",
        "ispb": "15114366",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "108",
        "code": "149",
        "name": "Facta CFI",
        "ispb": "15581638",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "103",
        "code": "142",
        "name": "Broker",
        "ispb": "16944141",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "120",
        "code": "184",
        "name": "Banco Itaú BBA",
        "ispb": "17298092",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "95",
        "code": "132",
        "name": "ICBC",
        "ispb": "17453575",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "92",
        "code": "129",
        "name": "UBS",
        "ispb": "18520834",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "91",
        "code": "128",
        "name": "MS Bank",
        "ispb": "19307785",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "125",
        "code": "194",
        "name": "Parmetal DTVM",
        "ispb": "20155248",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "111",
        "code": "163",
        "name": "Commerzbank",
        "ispb": "23522214",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "107",
        "code": "146",
        "name": "Guitta",
        "ispb": "24074692",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "86",
        "code": "120",
        "name": "Banco Rodobens",
        "ispb": "33603457",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "97",
        "code": "134",
        "name": "BGC Liquidez",
        "ispb": "33862244",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "80",
        "code": "111",
        "name": "Oliveira Trust",
        "ispb": "36113876",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "106",
        "code": "145",
        "name": "Levycam",
        "ispb": "50579044",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "101",
        "code": "139",
        "name": "Intesa Sanpaolo",
        "ispb": "55230916",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "81",
        "code": "113",
        "name": "Magliano CCVM",
        "ispb": "61723847",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "94",
        "code": "131",
        "name": "Tullett Prebon",
        "ispb": "61747085",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "102",
        "code": "140",
        "name": "Easynvest",
        "ispb": "62169875",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "116",
        "code": "177",
        "name": "Guide",
        "ispb": "65913436",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "112",
        "code": "169",
        "name": "Banco Olé Bonsucesso",
        "ispb": "71371686",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "131",
        "code": "217",
        "name": "Banco John Deere",
        "ispb": "91884981",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "83",
        "code": "117",
        "name": "Advanced Corretora",
        "ispb": "92856905",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "186",
        "code": "739",
        "name": "Banco Cetelem",
        "ispb": "00558456",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "88",
        "code": "124",
        "name": "Woori Bank",
        "ispb": "15357060",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "188",
        "code": "746",
        "name": "Banco Modal",
        "ispb": "30723886",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "154",
        "code": "399",
        "name": "Kirton Bank",
        "ispb": "01701201",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "153",
        "code": "394",
        "name": "Banco Bradesco Financiamentos",
        "ispb": "07207996",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "149",
        "code": "320",
        "name": "China Construction Bank",
        "ispb": "07450604",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "144",
        "code": "268",
        "name": "Barigui Companhia Hipotecária",
        "ispb": "14511781",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "167",
        "code": "545",
        "name": "Senso",
        "ispb": "17352220",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "146",
        "code": "271",
        "name": "IB CCTVM",
        "ispb": "27842177",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "136",
        "code": "241",
        "name": "Banco Clássico",
        "ispb": "31597552",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "166",
        "code": "505",
        "name": "Banco Credit Suisse",
        "ispb": "32062580",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "147",
        "code": "300",
        "name": "Banco de la Nacion Argentina",
        "ispb": "33042151",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "159",
        "code": "477",
        "name": "Citibank",
        "ispb": "33042953",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "143",
        "code": "266",
        "name": "Banco Cédula",
        "ispb": "33132044",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "150",
        "code": "366",
        "name": "Banco Société Générale",
        "ispb": "61533584",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "160",
        "code": "479",
        "name": "Banco ItauBank",
        "ispb": "60394079",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "142",
        "code": "265",
        "name": "Banco Fator",
        "ispb": "33644196",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "165",
        "code": "495",
        "name": "Bapro",
        "ispb": "44189447",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "162",
        "code": "488",
        "name": "JPMorgan Chase Bank",
        "ispb": "46518205",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "163",
        "code": "492",
        "name": "ING",
        "ispb": "49336860",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "140",
        "code": "250",
        "name": "BCV",
        "ispb": "50585090",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "141",
        "code": "253",
        "name": "Bexs Corretora de Câmbio",
        "ispb": "52937216",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "156",
        "code": "456",
        "name": "Banco MUFG Brasil",
        "ispb": "60498557",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "157",
        "code": "464",
        "name": "Banco Sumitomo Mitsui",
        "ispb": "60518222",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "151",
        "code": "370",
        "name": "Banco Mizuho",
        "ispb": "61088183",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "139",
        "code": "249",
        "name": "Banco Investcred Unibanco",
        "ispb": "61182408",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "175",
        "code": "626",
        "name": "Banco Ficsa",
        "ispb": "61348538",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "171",
        "code": "611",
        "name": "Banco Paulista",
        "ispb": "61820817",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "161",
        "code": "487",
        "name": "Deutsche Bank",
        "ispb": "62331228",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "135",
        "code": "233",
        "name": "Banco Cifra",
        "ispb": "62421979",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "133",
        "code": "222",
        "name": "Banco Credit Agrícole Brasil",
        "ispb": "75647891",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "255",
        "code": "342",
        "name": "Creditas sociedade de crédito direto s.a.",
        "ispb": "32997490",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "190",
        "code": "751",
        "name": "Scotiabank",
        "ispb": "29030467",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "181",
        "code": "652",
        "name": "Itaú Unibanco Holding",
        "ispb": "60872504",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "193",
        "code": "754",
        "name": "Banco Sistema",
        "ispb": "76543115",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "180",
        "code": "643",
        "name": "Banco Pine",
        "ispb": "62144175",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "989",
        "code": "449",
        "name": "Dmcard sociedade de crédito direto s.a.",
        "ispb": "37555231",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1093",
        "code": "555",
        "name": "Pan financeira s.a. - crédito, financiamento e investimentos",
        "ispb": "02682287",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1094",
        "code": "540",
        "name": "Facilicred sociedade de crédito ao microempreendedor ltda",
        "ispb": "04849745",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1095",
        "code": "548",
        "name": "Rpw s/a sociedade de crédito, financiamento e investimento",
        "ispb": "06249129",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1096",
        "code": "577",
        "name": "Desenvolve sp - agência de fomento do estado de são paulo s.a.",
        "ispb": "10663610",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1097",
        "code": "576",
        "name": "Mercado bitcoin instituicao de pagamento ltda",
        "ispb": "11351086",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1098",
        "code": "569",
        "name": "Conta pronta instituicao de pagamento ltda",
        "ispb": "12473687",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1099",
        "code": "549",
        "name": "Intra investimentos distribuidora de títulos e valores mobiliários ltda",
        "ispb": "15489568",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1100",
        "code": "562",
        "name": "Azimut brasil distribuidora de títulos e valores mobiliários ltda",
        "ispb": "18684408",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1101",
        "code": "538",
        "name": "Sudacred - sociedade de crédito ao microempreendedor e à empresa de pequeno porte ltda.",
        "ispb": "20251847",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1102",
        "code": "588",
        "name": "Prover promocao de vendas instituicao de pagamento ltda",
        "ispb": "20308187",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1103",
        "code": "533",
        "name": "Srm bank instituição de pagamento s/a",
        "ispb": "22575466",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1110",
        "code": "578",
        "name": "Cooperativa de crédito dos servidores públicos municipais da grande vitória/es",
        "ispb": "01235921",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1178",
        "code": "591",
        "name": "Banvox distribuidora de títulos e valores mobiliários ltda",
        "ispb": "02671743",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1194",
        "code": "554",
        "name": "Stonex banco de câmbio s.a.",
        "ispb": "28811341",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1195",
        "code": "557",
        "name": "Pagprime instituicao de pagamento ltda",
        "ispb": "30944783",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1196",
        "code": "567",
        "name": "Mercantil financeira s.a. - crédito, financiamento e investimento",
        "ispb": "33040601",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1197",
        "code": "583",
        "name": "Cooperativa central de crédito, poupança e investimento do centro norte do brasil - central sicredi centro norte",
        "ispb": "33667205",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1198",
        "code": "582",
        "name": "Cooperativa central de crédito, poupança e investimento de mato grosso do sul, goiás, distrito federal e tocantins - central sicredi brasil central",
        "ispb": "33737818",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1199",
        "code": "531",
        "name": "Bmp sociedade de crédito direto s.a",
        "ispb": "34337707",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1200",
        "code": "587",
        "name": "Fidd distribuidora de títulos e valores mobiliários ltda.",
        "ispb": "37678915",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1201",
        "code": "544",
        "name": "Multicred sociedade de crédito direto s.a.",
        "ispb": "38593706",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1202",
        "code": "563",
        "name": "Protege pay cash instituicao de pagamento s/a",
        "ispb": "40276692",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1203",
        "code": "556",
        "name": "Proseftur corretora de cambio s.a",
        "ispb": "40333582",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1204",
        "code": "305",
        "name": "Fourtrade corretora de câmbio ltda.",
        "ispb": "40353377",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1206",
        "code": "592",
        "name": "Instituição de pagamentos maps ltda.",
        "ispb": "45548763",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1207",
        "code": "558",
        "name": "Qi distribuidora de títulos e valores mobiliários ltda.",
        "ispb": "46955383",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1208",
        "code": "575",
        "name": "Dgbk credit s.a. - sociedade de crédito direto.",
        "ispb": "48584954",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1210",
        "code": "553",
        "name": "Percapital sociedade de crédito direto s.a.",
        "ispb": "48707451",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1211",
        "code": "551",
        "name": "Vert distribuidora de títulos e valores mobiliários ltda",
        "ispb": "48967968",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1212",
        "code": "559",
        "name": "Kanastra sociedade de crédito direto s.a.",
        "ispb": "49288113",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1213",
        "code": "579",
        "name": "Quadra sociedade de crédito direto s.a.",
        "ispb": "49555647",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1214",
        "code": "568",
        "name": "Brcondos sociedade de crédito direto s.a.",
        "ispb": "49933388",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1215",
        "code": "585",
        "name": "Sethi sociedade de crédito direto s.a.",
        "ispb": "50946592",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1216",
        "code": "589",
        "name": "G5 sociedade de crédito direto s.a.",
        "ispb": "51212088",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1217",
        "code": "620",
        "name": "Revolut sociedade de crédito direto s.a.",
        "ispb": "51342763",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1218",
        "code": "572",
        "name": "All in cred sociedade de credito direto s.a.",
        "ispb": "51414521",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1219",
        "code": "614",
        "name": "Nitro sociedade de crédito direto s.a.",
        "ispb": "52440987",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1220",
        "code": "644",
        "name": "321 sociedade de crédito direto s.a.",
        "ispb": "54647259",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1221",
        "code": "581",
        "name": "Cooperativa central de crédito, poupança e investimento do nordeste - central sicredi nordeste",
        "ispb": "70119680",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1222",
        "code": "514",
        "name": "Exim corretora de cambio ltda",
        "ispb": "73302408",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1223",
        "code": "565",
        "name": "Ágora corretora de titulos e valores mobiliarios s.a.",
        "ispb": "74014747",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1224",
        "code": "584",
        "name": "Cooperativa central de crédito, poupança e investimento dos estados do paraná, são paulo e rio de janeiro - central sicredi pr/sp/rj",
        "ispb": "80230774",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1225",
        "code": "580",
        "name": "Cooperativa central de crédito, poupança e investimento do sul e sudeste - central sicredi sul/sudeste",
        "ispb": "87437687",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1226",
        "code": "543",
        "name": "Cooperativa de economia e crédito mútuo dos eletricitários e dos trabalhadores das empresas do setor de energia - coopcrece",
        "ispb": "92825397",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1251",
        "code": "619",
        "name": "Trio instituicao de pagamento ltda.",
        "ispb": "49931906",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1255",
        "code": "599",
        "name": "Agoracred s/a sociedade de crédito, financiamento e investimento",
        "ispb": "36321990",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    },
    {
        "id": "1287",
        "code": "664",
        "name": "Eagle instituicao de pagamento ltda.",
        "ispb": "11414839",
        "image": "https://cdn.transfeera.com/banks/default_bank.svg",
        "spi_participant_type": None
    }
]
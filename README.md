# Poznej FI - Workshop - Od verzování až k automatickému nasazení 

Společně si zkusíme verzovat zdrojový kód a spolupracovat na něm. Následně ho ručně otestujeme a zařídíme, aby se testy spouštěly při každé změně. A pokud testy uspějí, zveřejníme automaticky novou verzi a nasadíme ji na náš server. V neposlední řadě si ukážeme, že Docker je elegantní způsob distribuce některých typů programů.

- Čas: 1h 30m
- Přístupové údaje: Pro zrychlení některé předem vygenerované (odkaz je na tabuli). Zkoušíte si to doma? Klidně si založte vlastní účty.
- Klíčová slova: git, pytest, CI/CD, Github Actions, Virtual Machine in Cloud, SSH, Docker

# Plán

## Úvod (5 min)

- Usazení (po dvojících)
- Představení plánu a [finálního stavu repositáře][branch-final], ukázka [historie](https://github.com/PoznejFIWorkshop/code-to-deployed-app/commits/main)
- Otevření informační stránky
- Přehled zkušeností účastníků

## Git (10 min, párově)

Výchozí stav: [logika](https://github.com/PoznejFIWorkshop/code-to-deployed-app/commit/76038c006d41a71fbd48325a961de1476737666c), [webserver](https://github.com/PoznejFIWorkshop/code-to-deployed-app/commit/8d4e6c2f45f0000cb0397fb8ce5493a7b424a203)

- ~~Nainstalování GitHub Desktop~~ _(připraveno předem)_
- ~~Založení GitHub účtu~~ _(připraveno předem)_
- Přihlášení do GitHub Desktop
- Představení ukázkového projektu (hlavně souboru `logic.py`) a [jeho repositáře (i.e. tohoto) na webu]((https://github.com/PoznejFIWorkshop/code-to-deployed-app/commits/main))
- GitHub Desktop (klonování repositáře)
- Každý pár účastníků si vytvoří vlastní větev na základě větve `initial` a přejde na svou individuální větev


## Testování (15 minut, párově)
- otevření VS Code a složky v něm
- každý pár účastníků vytvoří soubor `test_number1_number2.py` (nějaké čísla si vymyslete, jiná než ostatní)
- v GitHub Desktop: add changes, commit, push

- Pytest
    - instalace [Pytest](https://pypi.org/project/pytest/)
        - `python -m pip install pytest`
        - přidat řádek `pytest` do `requirements.txt`
            - `requirements.txt` lze nainstalovat pomocí `python -m pip install -r requirements.txt`
    - každý pár účastníků napíše nějaké testy používající `assert`
    - testy lze spustit pomocí: `python -m pytest .`
    - v GitHub Desktop: add changes, commit, push

- vysvětlení Pull Requestů, [založení jednoho](https://github.com/PoznejFIWorkshop/code-to-deployed-app/pulls)
- organizátor PR ověří a mergne do větve `demo`

[Diff](https://github.com/PoznejFIWorkshop/code-to-deployed-app/commit/28481fe0000dad3cacea1f6b2be8ed4f3274a544)

## Refactoring (5 minut, společně)
- přejít na větev `demo`, git pull, vytvořit si novou větev
- společně trochu vylepšíme `logic.py`
    - Chcete nápady? Zkuste [EduLint](https://edulint.com). Na tak malém kódu toho moc není, ale jako ukázka dobrý. :)
    - Můžete si na začátek souboru přidat řádek `# edulint: enhancement` a zapnou se ještě další kontroly.
- _Změny můžeme dělat v klidu, protože když něco rozbijeme, testy nám to řeknou a historie nám umožňuje to vrátit!_

[Diff](https://github.com/PoznejFIWorkshop/code-to-deployed-app/commit/3ff3df3f70f587982e8c32fdcfc042fe566a5988)


## Continuous integration (Github Actions) (10 minut, společně)
- Založení workflow souboru `.github/workflows/test-publish-deploy.yaml`
- Spuštění pytest ve workflow souboru
- Push do Gitu
- Zkontrolovat výsledek v Github Actions

[Diff](https://github.com/PoznejFIWorkshop/code-to-deployed-app/commit/d754b837c04b8f5f013cb7d7c7f0010dec0fe44d)

## Vzdálený server (10 minut, část ukázka, SSH a git clone párově)
- Virtual Machine v cloudu (na Cloudovém providerovi nezáleží)
- připojení na vzdálený server - SSH a základ Bashe
    - `ssh root@SOME_IP` nebo `ssh root@poznejfi.iamroot.eu`
    - při zadávání hesla to bude vypadat, jako by se nepsalo, ale jen je skryté
- každý si vytvoří vlastní složku a přejde do ní
    - `mkdir SOME_NAME`
    - `cd SOME_NAME`
- git clone repositář
    - `git clone https://github.com/PoznejFIWorkshop/code-to-deployed-app.git`
    - `cd code-to-deployed-app`
    - `git checkout YOUR_BRANCH_NAME`
- ukázka git sychronizace
    - lokálně (i.e. na PC ve škole)
        - drobná změna v kódu (klidně třeba jen přidání prázdného řádku)
        - v GitHub Desktop: add changes, commit, push
    - na vzdáleném serveru (i.e. skrz SSH): `git pull`

## Docker (30 minut, společně)

Základná myšlenka Dockeru: Zabalím svůj kód/program a vše co potřebuje tak, aby to šlo snadno spustit kdekoliv.

Příklad: Představme si, že můj kód potřebuje Python 3.10, několik balíčků nainstalovaných pomocí pipu a běží pouze na Linuxu. Všechny tři věci tedy zabalíme do tzv. image, který pak lze virtualizovaně spustit kdekoliv.

### Instalace Docker a Docker-compose
- ~~Nainstalovat Docker a Docker-compose~~ _(připraveno předem)_
    - _I na systémech kde je Docker nainstalovaný často docker-compose není by default nainstalovaný. Na Linuxu ho lze doinstalovat např. pomocí `apt install -y docker-compose`.


### Ukázky spouštění věcí zabalených do Dockeru

Pro programy s CLI nebo webovým rozhraním už to možná udělal někdo za nás. Pojďme si to na pár ukázat:

- příklad: [Librespeed](https://hub.docker.com/r/linuxserver/librespeed) - Vlastní test rychlosti sítě

```sh
docker run -d --name=librespeed -p 8081:80 -v ${PWD}/librespeed/config:/config --restart unless-stopped lscr.io/linuxserver/librespeed:latest
```
     
- příklad: [Python](https://hub.docker.com/_/python) libovolné verze izolovaný od hlavního systému 

```sh
docker run -it python:3.10
docker run -it python:3.10 bash
docker run -it --volume ${PWD}:/app --workdir /app python:3.10 bash
```

- dalších pár oblíbených aplikací: https://github.com/awesome-selfhosted/awesome-selfhosted

### Jak zabalíme do Dockeru náš projekt?
- Napíšeme soubor `Dockerfile` a `.dockerignore`
- Následně:

```sh
docker build --tag poznejfi1 .
docker run -it poznejfi1 pytest .
docker run -it -p 80:80 poznejfi1
docker run --detach -p 80:80 poznejfi1
```

[Diff](https://github.com/PoznejFIWorkshop/code-to-deployed-app/commit/5f034ca5759c29fa9ad8df879d1364f29d8e86a2)

### Jak si udělat spouštění ještě jednoduší? (docker-compose)

Konfigurační parametry si můžeme uložit do souboru a verzovat je! Docker-compose navíc usnadňuje propojení více Docker kontejnerů dohromady (např. aplikace + databáze).

Konfiguraci si uložíme do souboru: `docker-compose.yaml`. Pak stačí udělat:

```sh
docker-compose up --build --detach
docker-compose down
```

[Diff](https://github.com/PoznejFIWorkshop/code-to-deployed-app/commit/c96fb41f076c81056b6f0a075e9b2d6ea3577fd5)

       
## Continuos deployment (15 minut, společně)

Pojďme taky zveřejnit naše dílo! Budeme upravovat soubor `.github/workflows/test-publish-deploy.yaml`

- ~~Registrace na [Docker Hub](https://hub.docker.com) (nebo podobné, např. Github Registry)~~ _(připraveno předem)_
- ~~Vytvoření API tokenu pro Docker Hub~~ _(připraveno předem)_
- Nastavení Github Secrets (Docker API token, SSH přihlašovací údaje)

- CD: Deploy using git

[Diff](https://github.com/PoznejFIWorkshop/code-to-deployed-app/commit/35a0f61426fae9a167449dca2a32fc86b93c67e3)

- CD: Build image, push to registry
- CD: Deploy skript (docker-compose pull, docker-compose up)

[Diff](https://github.com/PoznejFIWorkshop/code-to-deployed-app/commit/c746789c574bb61601435d9b25bc729e3ddaa4eb)


## Velké upozornění nakonec

Nyní víte dostatek na to, abyste byli nebezpeční pro sebe i okolí! Vše co jsme si ale dnes ukázali se můžete doučit samostudiem, teď když víte, co je možné. Nezapomeňte při samostudiu na dostatečně silná hesla, šifrování, firewally, zálohování a to, že **Docker kontejnery jsou pouze dočasné, pouze věci namountované skrz volumes jsou věčné!**


[branch-final]: https://github.com/PoznejFIWorkshop/code-to-deployed-app/tree/main


<details>
  <summary>Pokud by zbyl čas, můžeme se podívat na další témata:</summary>

### Nextcloud

[NextCloud](https://hub.docker.com/r/linuxserver/nextcloud) image od LinuxServer.io:

```yaml
---
version: "2.1"
services:
  nextcloud:
    image: lscr.io/linuxserver/nextcloud:latest
    container_name: nextcloud
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
    volumes:
      - ./nextcloud/appdata:/config
      - ./nextcloud/data:/data
    ports:
      - 443:443
    restart: unless-stopped
```

Start chvilku trvá, pak dostupný na https://SOME_IP

### Git intermediate

- větve, merge, merge konflikty
- Github a privátní repositáře

### Linux

- ssh klíče

### Self-hosting gotchas

- Docker obchází firewall (jak UFW, tak některé pravidla z iptables)
- Jak dělat zálohy volumes
- Docker na Windows
- VPN vs Veřejně dostupné z internetu


### Cokoliv, co navrhnete

</details>


<details>
  <summary>Poznámky pro přednášejícího - co zařídit předem:</summary>

- Udělat kopii tohoto repositáře do lokace `~/example_project`
- Přihlašovací údaje na lokální PC
- Linux VM
- vytvořit větev `demo` na základě větve `initial`
- Přihlašovací údaje pro účastníky
    - GitHub účet
    - API klíč pro Docker Hub
    - napsat je do dokumentu, který se nasdílí s účastníky
    - připravit je do repository secrets
- Na serveru připravit: 

```sh
apt update
apt install -y docker-compose
docker pull python:3.10
docker pull python:3.10-slim-buster
docker pull lscr.io/linuxserver/librespeed:latest

cd ~
git clone https://github.com/PoznejFIWorkshop/code-to-deployed-app.git example_project
```

- na místě workshopu:
    - Na všechny PC nainstalovat GitHub Desktop (pozor - na FI se po každém odhlášení smaže)
    - Na tabuli napsat link na repositář a na přihlašovací údaje

</details>


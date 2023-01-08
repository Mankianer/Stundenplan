# Mankianer Plan

## Functionality

__TODO__
* [x] Create a list of plans
* [ ] Configure the plan
* [ ] Set up Context and Options
* [ ] Fill the plans

### Create a list of plans
Mit `mankianerplan.create_plans(*names, slot_mask, config=None)` können Pläne erstellt werden.
Die slot_mask wie der Plan aufgebaut ist. Dort werden alles Slots nach Tagen aufgelistet.
Wenn die Config nicht angegeben wird, wird die Standardkonfiguration verwendet.

__`slot_mask` Beispiel:__
```json
{
  "tag1": [1,2,3],
  "tag2": [1,2,3,4,5],
  "tag3": [-2,-1,0,1,2,3,4,5,10]
}

```

### Configure the plan
Die Konfiguration ist in jeden TablePlan object unter `config` zu finden.
Die Konfiguration ist ein dict mit folgenden Keys:
* `slot_generator`: Funktion, die einen Slot erstellt.`*`
* `slot_rating`: Funktion, die einen Slot bewertet.`*` Je höher die Bewertung, desto besser.
* `slot_filter`: Funktion, die einen Slot filtert.`*` Wenn `True` zurückgegeben wird, wird der Slot nicht verwendet.  

 `*` mit den erwarteten Optionen mit default Werten als Tupel.

#### Slot Generator
_ToDo: Slot Generator beschreiben_

#### Slot Rating
_ToDo: Slot Rating beschreiben_

#### Slot Filter
_ToDo: Slot Filter beschreiben_
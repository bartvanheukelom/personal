(function (root, factory) {
  if (typeof define === 'function' && define.amd)
    define(['exports'], factory);
  else if (typeof exports === 'object')
    factory(module.exports);
  else
    root['jsexport-toplevel'] = factory(typeof this['jsexport-toplevel'] === 'undefined' ? {} : this['jsexport-toplevel']);
}(this, function (_) {
  'use strict';
  Duck.prototype = Object.create(Bird.prototype);
  Duck.prototype.constructor = Duck;
  Chicken.prototype = Object.create(Bird.prototype);
  Chicken.prototype.constructor = Chicken;
  SchrodingersDuck.prototype = Object.create(AbstractBird.prototype);
  SchrodingersDuck.prototype.constructor = SchrodingersDuck;
  WildGooseChaseGoose.prototype = Object.create(AbstractBird.prototype);
  WildGooseChaseGoose.prototype.constructor = WildGooseChaseGoose;
  function Bird() {
  }
  Bird.prototype.layEgg_1 = function () {
  };
  Bird.$metadata$ = {
    simpleName: 'Bird',
    kind: 'class',
    interfaces: []
  };
  function AbstractBird() {
  }
  AbstractBird.prototype.layAbstractEgg_1 = function () {
  };
  AbstractBird.$metadata$ = {
    simpleName: 'AbstractBird',
    kind: 'class',
    interfaces: []
  };
  function Duck() {
    Bird.call(this);
  }
  Duck.prototype.swim = function () {
  };
  Duck.$metadata$ = {
    simpleName: 'Duck',
    kind: 'class',
    interfaces: []
  };
  function Chicken() {
    Bird.call(this);
  }
  Chicken.prototype.roost = function () {
  };
  Chicken.$metadata$ = {
    simpleName: 'Chicken',
    kind: 'class',
    interfaces: []
  };
  function SchrodingersDuck() {
    AbstractBird.call(this);
  }
  SchrodingersDuck.prototype.swimOrDont = function () {
  };
  SchrodingersDuck.$metadata$ = {
    simpleName: 'SchrodingersDuck',
    kind: 'class',
    interfaces: []
  };
  function WildGooseChaseGoose() {
    AbstractBird.call(this);
  }
  WildGooseChaseGoose.prototype.stressOut = function () {
  };
  WildGooseChaseGoose.$metadata$ = {
    simpleName: 'WildGooseChaseGoose',
    kind: 'class',
    interfaces: []
  };
  Duck.prototype.layEgg_1 = Bird.prototype.layEgg_1;
  Chicken.prototype.layEgg_1 = Bird.prototype.layEgg_1;
  SchrodingersDuck.prototype.layAbstractEgg_1 = AbstractBird.prototype.layAbstractEgg_1;
  WildGooseChaseGoose.prototype.layAbstractEgg_1 = AbstractBird.prototype.layAbstractEgg_1;
  _.Bird = Bird;
  _.Bird.Duck = Duck;
  _.Bird.Chicken = Chicken;
  _.AbstractBird = AbstractBird;
  _.AbstractBird.SchrodingersDuck = SchrodingersDuck;
  _.AbstractBird.WildGooseChaseGoose = WildGooseChaseGoose;
  return _;
}));

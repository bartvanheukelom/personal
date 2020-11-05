(function (root, factory) {
  if (typeof define === 'function' && define.amd)
    define(['exports'], factory);
  else if (typeof exports === 'object')
    factory(module.exports);
  else
    root['js-companion-notstatic'] = factory(typeof this['js-companion-notstatic'] === 'undefined' ? {} : this['js-companion-notstatic']);
}(this, function (_) {
  'use strict';
  Companion_1.prototype = Object.create(AWACompanion.prototype);
  Companion_1.prototype.constructor = Companion_1;
  function Classy() {
  }
  Classy.$metadata$ = {
    simpleName: 'Classy',
    kind: 'class',
    interfaces: []
  };
  function WA() {
  }
  WA.$metadata$ = {
    simpleName: 'WA',
    kind: 'class',
    interfaces: []
  };
  function AWACompanion() {
  }
  AWACompanion.prototype.workAroundTheClock_0 = function () {
  };
  AWACompanion.$metadata$ = {
    simpleName: 'AWACompanion',
    kind: 'class',
    interfaces: []
  };
  function _get_WACompanion_() {
    return Companion_getInstance_0();
  }
  function Companion_0() {
    Companion_instance = this;
  }
  Companion_0.prototype.beFriendly = function () {
  };
  Companion_0.$metadata$ = {
    simpleName: 'Companion',
    kind: 'object',
    interfaces: []
  };
  var Companion_instance;
  function Companion_getInstance() {
    if (Companion_instance == null)
      new Companion_0();
    return Companion_instance;
  }
  function Companion_1() {
    Companion_instance_0 = this;
    AWACompanion.call(this);
  }
  Companion_1.$metadata$ = {
    simpleName: 'Companion',
    kind: 'object',
    interfaces: []
  };
  var Companion_instance_0;
  function Companion_getInstance_0() {
    if (Companion_instance_0 == null)
      new Companion_1();
    return Companion_instance_0;
  }
  Companion_1.prototype.workAroundTheClock_0 = AWACompanion.prototype.workAroundTheClock_0;
  _.Classy = Classy;
  _.WA = WA;
  _.AWACompanion = AWACompanion;
  Object.defineProperty(_, 'WACompanion', {
    configurable: true,
    get: _get_WACompanion_
  });
  return _;
}));

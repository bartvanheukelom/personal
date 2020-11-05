(function (root, factory) {
  if (typeof define === 'function' && define.amd)
    define(['exports'], factory);
  else if (typeof exports === 'object')
    factory(module.exports);
  else
    root['jsexport-toplevel'] = factory(typeof this['jsexport-toplevel'] === 'undefined' ? {} : this['jsexport-toplevel']);
}(this, function (_) {
  'use strict';
  Exception.prototype = Object.create(Error.prototype);
  Exception.prototype.constructor = Exception;
  RuntimeException.prototype = Object.create(Exception.prototype);
  RuntimeException.prototype.constructor = RuntimeException;
  ClassCastException.prototype = Object.create(RuntimeException.prototype);
  ClassCastException.prototype.constructor = ClassCastException;
  Duck.prototype = Object.create(Bird.prototype);
  Duck.prototype.constructor = Duck;
  Chicken.prototype = Object.create(Bird.prototype);
  Chicken.prototype.constructor = Chicken;
  SchrodingersDuck.prototype = Object.create(AbstractBird.prototype);
  SchrodingersDuck.prototype.constructor = SchrodingersDuck;
  WildGooseChaseGoose.prototype = Object.create(AbstractBird.prototype);
  WildGooseChaseGoose.prototype.constructor = WildGooseChaseGoose;
  function getStringHashCode(str) {
    var hash = 0;
    var length = str.length;
    var inductionVariable = 0;
    var last = length - 1 | 0;
    if (inductionVariable <= last)
      do {
        var i = inductionVariable;
        inductionVariable = inductionVariable + 1 | 0;
        var code = str.charCodeAt(i);
        hash = imul(hash, 31) + code | 0;
      }
       while (!(i === last));
    return hash;
  }
  function captureStack(instance, constructorFunction) {
    if (Error.captureStackTrace != null) {
      Error.captureStackTrace(instance, constructorFunction);
    } else {
      instance.stack = (new Error()).stack;
    }
  }
  function extendThrowable(this_, message, cause) {
    Error.call(this_);
    setPropertiesToThrowableInstance(this_, message, cause);
  }
  function setPropertiesToThrowableInstance(this_, message, cause) {
    if (!hasOwnPrototypeProperty(this_, 'message')) {
      var tmp1_elvis_lhs = message;
      var tmp;
      if (tmp1_elvis_lhs == null) {
        var tmp0_safe_receiver = cause;
        tmp = tmp0_safe_receiver == null ? null : tmp0_safe_receiver.toString();
      } else {
        tmp = tmp1_elvis_lhs;
      }
      var tmp2_elvis_lhs = tmp;
      this_.message = tmp2_elvis_lhs == null ? undefined : tmp2_elvis_lhs;
    }if (!hasOwnPrototypeProperty(this_, 'cause')) {
      this_.cause = cause;
    }this_.name = Object.getPrototypeOf(this_).constructor.name;
  }
  function hasOwnPrototypeProperty(o, name) {
    var tmp0_unsafeCast_0 = Object.getPrototypeOf(o).hasOwnProperty(name);
    return tmp0_unsafeCast_0;
  }
  function THROW_CCE() {
    throw ClassCastException_init_$Create$();
  }
  function imul(a_local, b_local) {
    var lhs = jsBitwiseAnd(a_local, 4.29490176E9) * jsBitwiseAnd(b_local, 65535);
    var rhs = jsBitwiseAnd(a_local, 65535) * b_local;
    return jsBitwiseOr(lhs + rhs, 0);
  }
  function Exception() {
    captureStack(this, Exception);
  }
  Exception.$metadata$ = {
    simpleName: 'Exception',
    kind: 'class',
    interfaces: []
  };
  function RuntimeException() {
    captureStack(this, RuntimeException);
  }
  RuntimeException.$metadata$ = {
    simpleName: 'RuntimeException',
    kind: 'class',
    interfaces: []
  };
  function ClassCastException() {
    captureStack(this, ClassCastException);
  }
  ClassCastException.$metadata$ = {
    simpleName: 'ClassCastException',
    kind: 'class',
    interfaces: []
  };
  function Exception_init_$Init$($this) {
    extendThrowable($this, null, null);
    Exception.call($this);
    return $this;
  }
  function RuntimeException_init_$Init$($this) {
    Exception_init_$Init$($this);
    RuntimeException.call($this);
    return $this;
  }
  function ClassCastException_init_$Init$($this) {
    RuntimeException_init_$Init$($this);
    ClassCastException.call($this);
    return $this;
  }
  function ClassCastException_init_$Create$() {
    var tmp = ClassCastException_init_$Init$(Object.create(ClassCastException.prototype));
    captureStack(tmp, ClassCastException_init_$Create$);
    return tmp;
  }
  function jsBitwiseOr(lhs_hack, rhs_hack) {
    var tmp0_unsafeCast_0 = lhs_hack | rhs_hack;
    return tmp0_unsafeCast_0;
  }
  function jsBitwiseAnd(lhs_hack, rhs_hack) {
    var tmp0_unsafeCast_0 = lhs_hack & rhs_hack;
    return tmp0_unsafeCast_0;
  }
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
  function AnimalLike() {
  }
  AnimalLike.$metadata$ = {
    simpleName: 'AnimalLike',
    kind: 'interface',
    interfaces: []
  };
  function Android(memory) {
    this._memory = memory;
  }
  Android.prototype._get_memory_ = function () {
    return this._memory;
  };
  Android.prototype.component1 = function () {
    return this._memory;
  };
  Android.prototype.copy = function (memory) {
    return new Android(memory);
  };
  Android.prototype.copy$default = function (memory, $mask0, $handler) {
    var memory_0 = !(($mask0 & 1) === 0) ? this._memory : memory;
    return this.copy(memory_0);
  };
  Android.prototype.toString = function () {
    return '' + 'Android(memory=' + this._memory + ')';
  };
  Android.prototype.hashCode = function () {
    return getStringHashCode(this._memory);
  };
  Android.prototype.equals = function (other) {
    if (this === other)
      return true;
    if (!(other instanceof Android))
      return false;
    else {
    }
    var tmp0_other_with_cast = other instanceof Android ? other : THROW_CCE();
    if (!(this._memory === tmp0_other_with_cast._memory))
      return false;
    return true;
  };
  Android.$metadata$ = {
    simpleName: 'Android',
    kind: 'class',
    interfaces: []
  };
  Object.defineProperty(Android.prototype, 'memory', {
    configurable: true,
    get: Android.prototype._get_memory_
  });
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
  function CareTaker(a) {
    this._a = a;
  }
  CareTaker.prototype._get_a_ = function () {
    return this._a;
  };
  CareTaker.prototype.takeCare = function () {
  };
  CareTaker.$metadata$ = {
    simpleName: 'CareTaker',
    kind: 'class',
    interfaces: []
  };
  Object.defineProperty(CareTaker.prototype, 'a', {
    configurable: true,
    get: CareTaker.prototype._get_a_
  });
  function Cloner(template) {
    this._template = template;
  }
  Cloner.prototype._get_template_ = function () {
    return this._template;
  };
  Cloner.prototype.produceClone = function () {
    return this._template.copy$default(null, 1, null);
  };
  Cloner.$metadata$ = {
    simpleName: 'Cloner',
    kind: 'class',
    interfaces: []
  };
  Object.defineProperty(Cloner.prototype, 'template', {
    configurable: true,
    get: Cloner.prototype._get_template_
  });
  function Humanoid() {
  }
  Humanoid.$metadata$ = {
    simpleName: 'Humanoid',
    kind: 'interface',
    interfaces: []
  };
  function ClassyHumanoid(name) {
    this._name = name;
  }
  ClassyHumanoid.prototype._get_name__1 = function () {
    return this._name;
  };
  ClassyHumanoid.$metadata$ = {
    simpleName: 'ClassyHumanoid',
    kind: 'class',
    interfaces: []
  };
  Object.defineProperty(ClassyHumanoid.prototype, 'name', {
    configurable: true,
    get: ClassyHumanoid.prototype._get_name__1
  });
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
  _.Android = Android;
  _.Android.Cloner = Cloner;
  _.ClassyHumanoid = ClassyHumanoid;
  _.ClassyHumanoid.CareTaker = CareTaker;
  return _;
}));

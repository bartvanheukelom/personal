type Nullable<T> = T | null | undefined
export class Bird {
    private constructor();
    layEgg(): void;
}
export namespace Bird {
    class Duck extends Bird {
        constructor();
        swim(): void;
    }
    class Chicken extends Bird {
        constructor();
        roost(): void;
    }
}
export abstract class AbstractBird {
    constructor();
    layAbstractEgg(): void;
}
export namespace AbstractBird {
    class SchrodingersDuck extends AbstractBird {
        constructor();
        swimOrDont(): void;
    }
    class WildGooseChaseGoose extends AbstractBird {
        constructor();
        stressOut(): void;
    }
}
export interface AnimalLike {
    readonly name: string;
}
export namespace AnimalLike {
    class CareTaker {
        constructor(a: AnimalLike);
        readonly a: AnimalLike;
        takeCare(): void;
    }
}
export class Android {
    constructor(memory: string);
    readonly memory: string;
    component1(): string;
    copy(memory: string): Android;
    toString(): string;
    hashCode(): number;
    equals(other: Nullable<any>): boolean;
}
export namespace Android {
    class Cloner {
        constructor(template: Android);
        readonly template: Android;
        produceClone(): Android;
    }
}
export interface Humanoid {
    readonly name: string;
}
export namespace Humanoid {
    class CareTaker {
        constructor(h: Humanoid);
        readonly h: Humanoid;
        takeCare(): void;
    }
}
export class ClassyHumanoid {
    constructor(name: string);
    readonly name: string;
}
export namespace ClassyHumanoid {
    class CareTaker {
        constructor(h: Humanoid);
        readonly h: Humanoid;
        takeCare(): void;
    }
}
export as namespace jsexport_toplevel;
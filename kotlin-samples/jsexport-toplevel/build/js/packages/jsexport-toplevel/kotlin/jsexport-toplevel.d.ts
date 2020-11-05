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
export as namespace jsexport_toplevel;
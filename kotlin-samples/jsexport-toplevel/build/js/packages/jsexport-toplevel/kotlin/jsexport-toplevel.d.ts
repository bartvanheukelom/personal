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
export as namespace jsexport_toplevel;
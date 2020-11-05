type Nullable<T> = T | null | undefined
export class Classy {
    constructor();
    readonly Companion: {
        beFriendly(): void;
    };
}
export class WA {
    constructor();
    readonly Companion: {
    } & AWACompanion;
}
export abstract class AWACompanion {
    constructor();
    workAroundTheClock(): void;
}
export const WACompanion: AWACompanion;
export as namespace js_companion_notstatic;
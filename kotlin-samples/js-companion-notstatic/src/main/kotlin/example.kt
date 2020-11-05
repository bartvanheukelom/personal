@file:JsExport

class Classy {

    companion object {

        fun beFriendly() {}

    }

}


// workaround
class WA {
    companion object : AWACompanion()
}
abstract class AWACompanion {
    fun workAroundTheClock() {}
}
val WACompanion: AWACompanion get() = WA

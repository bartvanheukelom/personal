
@JsExport
abstract class Type<TCommon : Type<TCommon>>

@kotlin.Suppress("NON_EXPORTABLE_TYPE")
@JsExport
class Value<
        TCommon : Type<TCommon>,
        out TSpecific : TCommon
        >() :
        Comparable<Value<TCommon, *>>
{

    override fun compareTo(other: Value<TCommon, *>): Int =
            0

}

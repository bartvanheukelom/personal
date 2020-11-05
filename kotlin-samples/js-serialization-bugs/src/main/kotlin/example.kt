import kotlinx.serialization.*
import kotlinx.serialization.encoding.*
import kotlinx.serialization.json.*
import kotlinx.serialization.builtins.serializer

@Serializable(with = Card.Serializer::class)
data class Card<F : CardFace>(
    val face: F
) {

    class Serializer<F : CardFace>(
        private val faceSer: KSerializer<F>
    ) : KSerializer<Card<F>> {
        override val descriptor get() = String.serializer().descriptor

        override fun deserialize(decoder: Decoder): Card<F> =
            Card(faceSer.deserialize(decoder))
        override fun serialize(encoder: Encoder, value: Card<F>) =
            faceSer.serialize(encoder, value.face)
    }

}

@Serializable(with = CardFace.Companion::class)
sealed class CardFace {

    companion object : KSerializer<CardFace> {
        override val descriptor get() = String.serializer().descriptor

        override fun deserialize(decoder: Decoder): CardFace =
            when (decoder.decodeString()) {
                "ace" -> Ace
                "joker" -> Joker
                else -> throw IllegalArgumentException()
            }
        override fun serialize(encoder: Encoder, value: CardFace) =
            encoder.encodeString(when(value) {
                Ace -> "ace"
                Joker -> "joker"
            })
    }

}

@Serializable
data class Hand(
    val cards: List<Card<CardFace>>
)

fun main() {

    Json.Default.encodeToString(Hand(listOf(
        Card(CardFace.Ace),
        Card(CardFace.Ace),
        Card(CardFace.Joker)
    )))
        .let(::println)

    Json.Default.encodeToString(CardFace.Ace as CardFace)
        .let(::println)

    Json.Default.encodeToString(Card(CardFace.Ace) as Card<CardFace>)
        .let(::println)

}

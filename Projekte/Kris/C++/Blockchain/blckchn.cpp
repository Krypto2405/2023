#include <iostream>
#include <vector>
#include <ctime>
#include <cstdint>
#include <openssl/sha.h>
#include <openssl/evp.h>
#include <openssl/rand.h>

// Definition of a block
struct Block {
    int index;
    std::time_t timestamp;
    std::string data;
    std::string previousHash;
    std::string hash;

    Block(int idx, std::time_t time, const std::string& data, const std::string& prevHash)
        : index(idx), timestamp(time), data(data), previousHash(prevHash) {
            hash = calculateHash();
        }

    std::string calculateHash() const {
        std::string dataToHash = std::to_string(index) + std::to_string(timestamp) + data + previousHash;
        unsigned char hash[SHA256_DIGEST_LENGTH];
        SHA256((unsigned char*)dataToHash.c_str(), dataToHash.size(), hash);
        std::string hashStr(reinterpret_cast<char*>(hash), SHA256_DIGEST_LENGTH);
        return hashStr;
    }
};

// Definition of the blockchain
class Blockchain {
private:
    std::vector<Block> chain;
    int coinLimit;

public:
    Blockchain(int limit) : coinLimit(limit) {
        // Create the genesis block
        Block genesisBlock(0, std::time(nullptr), "Genesis Block", "0");
        chain.push_back(genesisBlock);
    }

    const Block& getLatestBlock() const {
        return chain.back();
    }

    bool isCoinLimitReached() const {
        return chain.size() >= coinLimit;
    }

    void addBlock(const std::string& data) {
        if (isCoinLimitReached()) {
            std::cout << "Coin limit reached. No more blocks can be added." << std::endl;
            return;
        }

        const Block& previousBlock = getLatestBlock();
        Block newBlock(previousBlock.index + 1, std::time(nullptr), data, previousBlock.hash);
        chain.push_back(newBlock);
    }
};

// Function to encrypt a message using AES-256
std::string encryptMessage(const std::string& message, const std::string& key) {
    std::string encryptedMessage;
    unsigned char iv[EVP_MAX_IV_LENGTH];
    RAND_bytes(iv, EVP_MAX_IV_LENGTH);

    EVP_CIPHER_CTX* ctx = EVP_CIPHER_CTX_new();
    EVP_EncryptInit_ex(ctx, EVP_aes_256_cbc(), nullptr, (const unsigned char*)key.c_str(), iv);

    int ciphertextLen = message.size() + EVP_MAX_BLOCK_LENGTH;
    unsigned char* ciphertext = new unsigned char[ciphertextLen];

    int len;
    EVP_EncryptUpdate(ctx, ciphertext, &len, (const unsigned char*)message.c_str(), message.size());
    ciphertextLen = len;

    EVP_EncryptFinal_ex(ctx, ciphertext + len, &len);
    ciphertextLen += len;

    encryptedMessage = std::string((char*)iv, EVP_MAX_IV_LENGTH) + std::string((char*)ciphertext, ciphertextLen);

    EVP_CIPHER_CTX_free(ctx);
    delete[] ciphertext;

    return encryptedMessage;
}

// Function to decrypt a message using AES-256
std::string decryptMessage(const std::string& encryptedMessage, const std::string& key) {
    std::string decryptedMessage;
    unsigned char iv[EVP_MAX_IV_LENGTH];
    unsigned char* ciphertext = new unsigned char[encryptedMessage.size() - EVP_MAX_IV_LENGTH];

    memcpy(iv, encryptedMessage.c_str(), EVP_MAX_IV_LENGTH);
    memcpy(ciphertext, encryptedMessage.c_str() + EVP_MAX_IV_LENGTH, encryptedMessage.size() - EVP_MAX_IV_LENGTH);

    EVP_CIPHER_CTX* ctx = EVP_CIPHER_CTX_new();
    EVP_DecryptInit_ex(ctx, EVP_aes_256_cbc(), nullptr, (const unsigned char*)key.c_str(), iv);

    int plaintextLen = encryptedMessage.size() - EVP_MAX_IV_LENGTH + EVP_MAX_BLOCK_LENGTH;
    unsigned char* plaintext = new unsigned char[plaintextLen];

    int len;
    EVP_DecryptUpdate(ctx, plaintext, &len, ciphertext, encryptedMessage.size() - EVP_MAX_IV_LENGTH);
    plaintextLen = len;

    EVP_DecryptFinal_ex(ctx, plaintext + len, &len);
    plaintextLen += len;

    decryptedMessage = std::string((char*)plaintext, plaintextLen);

    EVP_CIPHER_CTX_free(ctx);
    delete[] plaintext;
    delete[] ciphertext;

    return decryptedMessage;
}

int main() {
    // Create a new blockchain with a coin limit of 2,000,000
    Blockchain blockchain(2000000);

    // Add blocks to the blockchain
    blockchain.addBlock("Block 1 Data");
    blockchain.addBlock("Block 2 Data");
    blockchain.addBlock("Block 3 Data");

    // Encrypt and decrypt a message
    std::string message = "This is a secret message.";
    std::string key = "MySecretKey";

    std::string encryptedMessage = encryptMessage(message, key);
    std::cout << "Encrypted Message: " << encryptedMessage << std::endl;

    std::string decryptedMessage = decryptMessage(encryptedMessage, key);
    std::cout << "Decrypted Message: " << decryptedMessage << std::endl;

    return 0;
}

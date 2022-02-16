// module for secure cryptographics hashes and streamlined password class

var SHA256 = require("crypto-js/sha256");


export let sha256_hash = (str: string) => {
	return SHA256(str).toString();
}

export class Hash {
	protected plain?: string;
	value: string;

	constructor(value: string, store_plain: boolean = false) {
		if (store_plain == true) {
			this.plain = value
		}

		this.value = SHA256(value).toString();
	}
}

export class Password {
	private hashObj: Hash;
	hash: string;


	compare(toCompare: string) {
		let hashed = new Hash(toCompare).value;
		return hashed == this.hash;
	}

	change(oldPass: string, newPass: string) {
		let oldHash = new Hash(oldPass).value;
		if (oldHash == this.hash) {
			let newHash: Hash = new Hash(newPass);
			this.hashObj = newHash;
			this.hash = newHash.value;
		}
	}


	constructor(value: string, store_plain: boolean = false) {
		let createdHash: Hash = new Hash(value, store_plain);
		this.hashObj = createdHash;
		this.hash = createdHash.value;
	}
}
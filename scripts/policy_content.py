"""Content of the five FICTIONAL ShopEase policy documents.
Each section is (heading, [blocks]); a block is a paragraph (str) or a bullet list (list[str])."""

META = "Version 2.0  |  Effective 1 January 2026  |  Owner: ShopEase Customer Experience Team  |  Fictional company for an academic assignment"

DOCS = {}

# ----------------------------------------------------------------------------------------------
DOCS["refund_returns_policy.pdf"] = ("ShopEase Refund and Returns Policy", "Policy ID SE-POL-01", [
 ("1. Purpose and scope", [
  "This policy explains when and how ShopEase customers can return products and receive refunds. It applies to all orders "
  "placed on the ShopEase website and mobile app and delivered within India. Cancellations before delivery are covered "
  "by the ShopEase Order Cancellation and Modification Policy, and payment-related refund questions are also covered by "
  "the ShopEase Payment, Billing and Invoice Policy."]),
 ("2. Return eligibility and the 30-day return window", [
  "ShopEase customers may return most items within 30 days of delivery. The 30 days are counted from the date shown as "
  "'Delivered' in the order tracking page. Returns requested after the 30-day window are not accepted, except where an item "
  "arrived damaged, defective or incorrect and was reported on time under Section 4.",
  "To be eligible for a return, an item must meet all of the following conditions:",
  ["The item is unused, unwashed and unaltered.", "The item is in its original packaging with all tags, labels, accessories and free gifts attached.",
   "The customer can identify the order by its order number.", "The item is not on the list of non-returnable items in Section 5."],
  "Shorter windows apply to some categories. Electronics and small appliances can be returned within 10 days of delivery, "
  "and only if the seal is intact or the product is faulty. Footwear must be returned unworn with the original box. "
  "Large furniture can be returned within 15 days and must be unassembled unless it is defective."]),
 ("3. Reasons for return and who bears the cost", [
  "ShopEase accepts returns for the following reasons: wrong size or fit, changed mind, item not as described, damaged item, "
  "defective item and wrong item delivered. ShopEase arranges a free reverse pickup for every eligible return in serviceable "
  "pincodes. If pickup is not available in the customer's area, the customer may send the item by any courier and ShopEase "
  "reimburses courier charges up to Rs. 150 on submission of the courier receipt. ShopEase does not charge a restocking fee "
  "on eligible returns."]),
 ("4. Damaged, defective or wrong items", [
  "If an item arrives damaged, defective or different from what was ordered, the customer must report it within 48 hours of "
  "delivery. The report must include the order number and clear photographs of the item, its packaging and the shipping label. "
  "For high-value items, an unboxing video is recommended.",
  "After verification, ShopEase arranges a free pickup and offers the customer a choice between a full refund, including the "
  "original shipping charge, and a replacement. If the replacement is out of stock, a full refund is issued. Reports made after "
  "48 hours are reviewed case by case and may be treated as normal returns within the 30-day window."]),
 ("5. Items that cannot be returned", [
  "The following items cannot be returned or exchanged unless they are damaged, defective or wrong on arrival:",
  ["Innerwear, socks, swimwear and other hygiene-sensitive clothing.", "Personalised, engraved or made-to-order products.",
   "Perishable goods such as food and flowers.", "Gift cards, vouchers and digital products.",
   "Opened cosmetics, personal-care products and earphones with broken hygiene seals.", "Items marked 'Final Sale' on the product page."]]),
 ("6. How to request a return", [
  "A return is requested under Account, then Orders, then Return Item. The customer selects the item, chooses a reason and "
  "uploads photographs when required. ShopEase schedules a pickup within 2 business days of approval. The courier attempts "
  "pickup up to 3 times; after 3 failed attempts the return request is closed and the customer may raise a new request "
  "within the original 30-day window. The customer should pack the item securely in its original packaging and hand over "
  "the return slip that is emailed after approval."]),
 ("7. Inspection of returned items", [
  "Returned items are inspected at the ShopEase warehouse within 2 business days of receipt. There are three possible outcomes. "
  "Approved: the full refund is released. Partially approved: if the item is used, washed or has missing parts, ShopEase may issue a "
  "partial refund of 50 to 80 percent of the item price and will explain the deduction by email. Rejected: if the item does not "
  "match what was shipped or shows signs of misuse beyond reasonable testing, the refund is declined and the item is sent back "
  "to the customer, who pays the return shipping charge."]),
 ("8. Refund timelines and refund methods", [
  "After a returned item passes warehouse inspection, ShopEase refunds the money to the original payment method within "
  "5 to 7 business days for credit cards, debit cards, UPI and net banking. Refunds to a ShopEase wallet or as store credit are "
  "completed within 24 hours of approval.",
  "For Cash on Delivery orders, the refund is sent by bank transfer within 7 to 10 business days. The customer must share "
  "bank account details through the Orders page so that the transfer can be made. Alternatively the customer may choose "
  "instant store credit.",
  "ShopEase cannot control how quickly a bank displays a refund on a statement. If a refund has not been received after 10 business "
  "days, the customer should contact support with the order number and the return tracking number so that ShopEase can "
  "share the bank reference number (ARN or UTR) for the refund."]),
 ("9. Tracking a refund", [
  "Customers can track a refund under Account, then Orders, then Refund Status. The statuses are Return Requested, Pickup "
  "Scheduled, Picked Up, Received at Warehouse, Inspection Complete, Refund Initiated and Refund Completed. Email and SMS "
  "notifications are sent when the status changes to Refund Initiated and Refund Completed."]),
 ("10. Exchanges", [
  "Size and colour exchanges are available within 30 days of delivery, subject to stock. Each item qualifies for one free "
  "exchange. If the requested size or colour is not available, the customer receives a refund instead. Price differences "
  "between the original and the new item are charged or refunded."]),
 ("11. Undelivered and refused parcels", [
  "If a parcel cannot be delivered after 3 attempts, or the customer refuses delivery, the parcel is returned to the ShopEase warehouse. "
  "The order amount, including shipping charges for prepaid orders, is refunded within 7 business days after the warehouse receives "
  "the parcel."]),
 ("12. Discounts, coupons and gift orders", [
  "When an order that used a coupon is partly returned, the coupon value is deducted from the refund in proportion to the price "
  "of the returned items. For gifts, the refund is issued to the person who paid for the order unless the purchaser requests "
  "store credit for the recipient."]),
 ("13. Abuse of the returns process", [
  "ShopEase may review accounts that make more than 8 returns in any 90-day period or that return used items repeatedly. Review "
  "may result in refunds being held until inspection is complete, limits on Cash on Delivery or, in serious cases, account restrictions."]),
 ("14. Quick reference", [
  ["Standard return window: 30 days from delivery. Electronics: 10 days. Furniture: 15 days.", "Damaged or defective items: report within 48 hours.",
   "Refund to card, UPI or net banking: 5 to 7 business days after inspection. Cash on Delivery: 7 to 10 business days by bank transfer.",
   "Wallet or store credit refund: within 24 hours. No restocking fee.", "If a refund has not arrived after 10 business days, contact support with the order number and the return tracking number."]]),
])

# ----------------------------------------------------------------------------------------------
DOCS["shipping_delivery_policy.pdf"] = ("ShopEase Shipping and Delivery Policy", "Policy ID SE-POL-02", [
 ("1. Purpose and serviceable areas", [
  "This policy describes how ShopEase ships orders, what delivery options and charges apply, and what customers can do if a "
  "delivery is late, failed or lost. ShopEase delivers to more than 19,000 pincodes across India. Customers can check whether "
  "their area is serviceable by entering the pincode on the product page. ShopEase does not currently ship outside India."]),
 ("2. Delivery options and delivery times", [
  "Standard delivery takes 3 to 5 business days in the four metro cities (Chennai, Mumbai, Delhi and Bengaluru) and 5 to 8 "
  "business days in all other serviceable locations. Express delivery takes 1 to 2 business days and costs Rs. 149. Next-day "
  "delivery is available in the four metro cities for orders placed before 2 PM and costs Rs. 199.",
  "Business days are Monday to Saturday, excluding public holidays. Delivery time starts counting from the dispatch date, not "
  "from the order date. The estimated delivery date shown at checkout is a promise date that ShopEase works to meet."]),
 ("3. Shipping charges", [
  "Shipping is free on orders above Rs. 999, calculated on the order value after discounts. Orders of Rs. 999 or less pay Rs. 59 "
  "for standard shipping. Express and next-day charges always apply in addition. Members of ShopEase Plus receive free standard "
  "shipping on all orders regardless of order value. Shipping charges are shown before payment and are never added later."]),
 ("4. Order processing and dispatch", [
  "Orders confirmed and paid before 2 PM on a business day are normally dispatched the same day. Orders confirmed after 2 PM "
  "are dispatched on the next business day. Cash on Delivery orders may need a verification call or SMS, which can add up to "
  "one business day. Pre-order items are dispatched on the date stated on the product page. ShopEase sends a dispatch "
  "notification by SMS and email when the parcel leaves the warehouse."]),
 ("5. Tracking an order", [
  "A tracking link is sent by SMS and email when the order is dispatched. Tracking updates may take up to 12 hours to appear "
  "after dispatch. Tracking is also available under Account, then Orders. The statuses are Processing, Packed, Dispatched, "
  "In Transit, Out for Delivery, Delivered and Delivery Attempt Failed. If the tracking page shows no movement for more than "
  "48 hours after dispatch, the customer can contact support for a courier investigation."]),
 ("6. Changing the delivery address", [
  "The shipping address can be changed before dispatch under Account, then Orders, then Edit Address. After dispatch the address "
  "cannot be changed, because the parcel is already labelled and with the courier. If the address was wrong, the customer may "
  "refuse delivery and ShopEase will refund the order after the parcel returns to the warehouse, or may ask the courier to "
  "reschedule delivery once for up to 3 days later.",
  "A second delivery address, for example an office or a family member's home, can be saved under Account, then Address Book. "
  "The customer can choose any saved address at checkout."]),
 ("7. Delivery attempts and failed deliveries", [
  "The courier makes up to 3 delivery attempts on consecutive business days. The customer receives an SMS before each attempt. "
  "If the customer is unavailable, the delivery can be rescheduled once through the tracking link. After 3 failed attempts the "
  "parcel returns to the ShopEase warehouse and the refund process in the Refund and Returns Policy applies. Repeated refusal "
  "of Cash on Delivery parcels can lead to Cash on Delivery being disabled for the account."]),
 ("8. Delivery verification", [
  "For Cash on Delivery orders and for any order above Rs. 10,000, the courier asks for a one-time password (OTP) sent to the "
  "registered mobile number. The customer should share the OTP only with the courier at the time of handover. ShopEase never asks "
  "for an OTP by phone, email or chat."]),
 ("9. Late deliveries", [
  "If an order is not delivered within 3 days of the promised delivery date, the customer may contact support for a priority "
  "investigation or cancel the order for a full refund. For express and next-day orders delivered later than the promised date, "
  "ShopEase refunds the express or next-day shipping charge automatically."]),
 ("10. Lost parcels and parcels damaged in transit", [
  "If the tracking page shows 'Delivered' but the customer has not received the parcel, the customer should report it within 3 days. "
  "ShopEase investigates with the courier for up to 5 business days and then sends a replacement or issues a full refund. "
  "If a parcel looks tampered with or damaged at the time of delivery, the customer should photograph it, preferably refuse "
  "to accept it, and report within 48 hours. Damaged items follow the process in the Refund and Returns Policy."]),
 ("11. Split shipments", [
  "Orders with several items may ship in more than one parcel from different warehouses. Each parcel has its own tracking link. "
  "Shipping charges are applied once per order, and an order is considered delivered when all parcels are delivered."]),
 ("12. Delays beyond ShopEase's control", [
  "Deliveries may be delayed by severe weather, strikes, natural disasters, festival peak periods, road closures and government "
  "restrictions. ShopEase will notify affected customers by SMS or email and update the promised date. Where a delay exceeds "
  "7 days, the customer may cancel for a full refund."]),
])

# ----------------------------------------------------------------------------------------------
DOCS["order_cancellation_policy.pdf"] = ("ShopEase Order Cancellation and Modification Policy", "Policy ID SE-POL-03", [
 ("1. Purpose and scope", [
  "This policy sets out when customers can cancel or change a ShopEase order, the fees that apply, and how cancellations of "
  "memberships and newsletters work. Returns after delivery are covered by the Refund and Returns Policy."]),
 ("2. Cancelling before dispatch is free", [
  "Orders cancelled before dispatch are cancelled free of charge and refunded in full, including shipping charges and any "
  "payment gateway charges. Prepaid orders are refunded to the original payment method within 5 to 7 business days, or to a "
  "ShopEase wallet within 24 hours if the customer chooses that option. Cash on Delivery orders cancelled before dispatch have "
  "nothing to refund because no payment has been collected."]),
 ("3. Cancelling after dispatch", [
  "Orders cancelled after dispatch incur a handling fee of Rs. 99, which is deducted from the refund. Once an order is dispatched "
  "the courier has already collected it, so the parcel must travel back to the warehouse. The customer can cancel after dispatch "
  "by contacting support or by refusing the delivery. The refund, minus the Rs. 99 handling fee, is issued within 5 to 7 "
  "business days after the warehouse receives the parcel. After delivery, an order cannot be cancelled and must be returned under "
  "the Refund and Returns Policy."]),
 ("4. How to cancel an order", [
  "To cancel, the customer opens Account, then Orders, selects the order and chooses Cancel. Customers can also type 'cancel order' "
  "in the support chat or contact support by phone. If the order status is Packed, the cancellation may take up to 2 hours "
  "to be confirmed, and if the parcel is handed to the courier in that time the dispatch rules in Section 3 apply. The customer "
  "receives an email when the cancellation is confirmed."]),
 ("5. Partial cancellation of multi-item orders", [
  "Individual items can be cancelled before dispatch. If the remaining items no longer reach the free-shipping threshold of "
  "Rs. 999, the standard shipping charge of Rs. 59 is applied to the remaining order and deducted from the refund. When the whole "
  "order is cancelled before dispatch, the shipping charge is refunded."]),
 ("6. Changing an order before dispatch", [
  "Before dispatch, the customer can change the size, colour or quantity of an item, subject to stock, and can update the delivery "
  "address. After dispatch, items and quantities cannot be changed. The payment method of an order cannot be changed; the customer "
  "should cancel the order and place a new one. Price differences are charged or refunded."]),
 ("7. Personalised and made-to-order items", [
  "Personalised products can be cancelled only within 2 hours of placing the order, before production starts. After that time "
  "they cannot be cancelled or returned unless they are damaged or defective."]),
 ("8. Cancellations made by ShopEase", [
  "ShopEase may cancel an order if an item is out of stock, if a price was shown incorrectly, if the delivery address is not "
  "serviceable, or if the order fails fraud verification. The customer is informed by email and SMS and receives a full refund "
  "within 5 to 7 business days. No handling fee applies when ShopEase cancels."]),
 ("9. Cash on Delivery refusals", [
  "If a customer refuses 3 Cash on Delivery parcels within 6 months, Cash on Delivery is disabled for the account and the "
  "customer must use prepaid payment methods."]),
 ("10. ShopEase Plus membership cancellation", [
  "ShopEase Plus members can cancel at any time under Account, then Membership. Annual memberships cancelled within 7 days of "
  "purchase, with no member benefits used, are refunded in full. After 7 days no refund is given, but benefits continue until the "
  "end of the paid period. Monthly memberships stop renewing from the next billing date."]),
 ("11. Unsubscribing from the newsletter", [
  "Customers can unsubscribe using the link at the bottom of any ShopEase newsletter, or by changing the preference under "
  "Account, then Notifications. The change takes effect within 2 days. Order and shipping messages continue because they are "
  "service messages and not marketing."]),
 ("12. Cancellation fee summary", [
  ["Before dispatch: no fee, full refund.", "After dispatch: handling fee of Rs. 99 deducted from the refund.",
   "After delivery: no cancellation; use the return process.", "Personalised items: cancel within 2 hours of ordering.",
   "Cancelled by ShopEase: no fee, full refund."]]),
])

# ----------------------------------------------------------------------------------------------
DOCS["payment_billing_invoice_policy.pdf"] = ("ShopEase Payment, Billing and Invoice Policy", "Policy ID SE-POL-04", [
 ("1. Purpose and scope", [
  "This policy describes the payment methods ShopEase accepts, how payment problems are handled, and how invoices and tax "
  "documents are issued. Refund timelines are described in the Refund and Returns Policy."]),
 ("2. Accepted payment methods", [
  "ShopEase accepts credit and debit cards (Visa, Mastercard, RuPay and American Express), UPI, net banking from major banks, "
  "wallets, ShopEase gift cards and store credit. Cash on Delivery is available for orders up to Rs. 5000 and carries a "
  "handling fee of Rs. 30 per order. EMI on eligible credit cards is available for orders above Rs. 3000 with 3, 6 or 9 month "
  "tenures; interest rates are set by the card issuer and shown at checkout."]),
 ("3. Prices and taxes", [
  "All prices on ShopEase are in Indian rupees and include GST. The final payable amount, including shipping and any fees, is "
  "shown on the order summary before payment. ShopEase does not offer price matching or price adjustments after an order is placed."]),
 ("4. Payment security", [
  "Card payments are processed by PCI-DSS compliant payment partners. ShopEase does not store full card numbers or CVV codes. "
  "Payments are authenticated by the customer's bank with an OTP or a UPI PIN. ShopEase staff will never ask for a card number, "
  "PIN, OTP or password. Customers who receive such a request should treat it as fraud and report it to security@shopease.example."]),
 ("5. Failed payments where money is deducted", [
  "If a payment fails or the order is not confirmed but the money is deducted, the amount is automatically reversed to the "
  "customer's account within 3 to 5 business days. The customer should not pay again until the order status is checked under "
  "Account, then Orders. If the amount is not reversed after 5 business days, the customer should contact support with the "
  "transaction ID or UTR and a screenshot of the bank statement. Tickets about deducted money are treated as High priority."]),
 ("6. Duplicate or double charges", [
  "If a customer was charged twice for the same order, support investigates within 48 hours once the customer provides the "
  "transaction ID and the statement screenshot. A confirmed duplicate charge is refunded to the original payment method "
  "within 5 to 7 business days. The customer should not attempt to dispute the charge with the bank until the 48-hour investigation "
  "is complete."]),
 ("7. Cash on Delivery rules", [
  "Cash on Delivery is available only for orders up to Rs. 5000 and in serviceable pincodes. The customer should keep the exact "
  "amount ready because couriers may not carry change. UPI payment at the door is accepted by most couriers. Orders above "
  "Rs. 5000 must be paid online."]),
 ("8. Invoices", [
  "A GST invoice is emailed to the customer when the order is dispatched. Invoices can be downloaded under Account, then "
  "Orders for 24 months after the order date. A duplicate invoice can be requested from support and is sent within 1 business day. "
  "Customers who need a GST invoice with a business name and GSTIN must enter the GSTIN at checkout, because it cannot be added "
  "after the invoice is generated."]),
 ("9. Invoice corrections", [
  "Errors in the name, address or GSTIN can be corrected within 7 days of the invoice date. ShopEase issues a credit note for the "
  "original invoice and a new corrected invoice. After 7 days corrections are possible only where tax rules allow. Invoices cannot "
  "be changed to show a different amount or a different product."]),
 ("10. Store credit and gift cards", [
  "ShopEase gift cards and store credit are valid for 12 months from the date of issue, cannot be exchanged for cash and are "
  "not refundable. Store credit issued as a refund follows the same validity period."]),
 ("11. Coupons and promotional codes", [
  "One coupon can be used per order unless the offer says otherwise. Coupons cannot be combined, are not valid on gift cards and "
  "have no cash value. When items bought with a coupon are returned, the coupon value is deducted from the refund in proportion."]),
 ("12. Bank disputes and chargebacks", [
  "Customers are encouraged to contact ShopEase support before raising a dispute with their bank. If a chargeback is raised, "
  "ShopEase responds to the bank within 7 days with proof of delivery and order details. Orders under dispute may be put on hold "
  "and the account may be limited until the dispute is closed."]),
 ("13. Fraud prevention and verification", [
  "ShopEase screens orders for fraud. A flagged order may need ID or payment verification. If verification is not completed within "
  "24 hours, the order is cancelled and refunded in full within 5 to 7 business days."]),
 ("14. Billing support and response times", [
  "Billing and payment issues can be raised by chat, phone or email. Tickets where money has been deducted or charged twice receive "
  "a first response within 4 hours. Other billing questions receive a response within 24 hours."]),
])

# ----------------------------------------------------------------------------------------------
DOCS["account_complaints_escalation_policy.pdf"] = ("ShopEase Account Management, Complaints and Escalation Policy", "Policy ID SE-POL-05", [
 ("1. Purpose and scope", [
  "This policy explains how ShopEase customer accounts are created, protected and deleted, how customers can contact support, "
  "and how complaints are handled and escalated. It also defines the priority levels used by the support team."]),
 ("2. Creating an account", [
  "A ShopEase account requires a valid email address or mobile number, verified with a one-time password (OTP) that is valid for "
  "10 minutes. Customers must be at least 18 years old. Only one account is allowed per mobile number. If registration fails, the "
  "customer should check the spelling of the email address, confirm the mobile number is not already registered and request a new OTP."]),
 ("3. Logging in and password reset", [
  "Customers who forget a password use the Forgot Password link on the login page. The reset link is valid for 30 minutes and is "
  "sent to the registered email address. After 5 wrong password attempts the account is locked for 30 minutes. Customers who no "
  "longer have access to their registered email should contact support, which will verify identity before changing the email."]),
 ("4. Updating account details", [
  "Name, mobile number, addresses and notification preferences can be changed under Account, then Profile. Changing the email "
  "address or mobile number requires an OTP sent to the current contact. Customers are encouraged to switch on two-step "
  "verification under Account, then Security."]),
 ("5. Account deletion", [
  "Customers can request account deletion under Settings, then Privacy. The request is processed within 14 days and personal data "
  "is erased within 30 days. Pending orders and refunds must be completed first. Invoices and transaction records may be kept for "
  "the period required by tax law. Deletion cannot be undone once processed, and a new account must be created. Customers who "
  "want a break can choose temporary deactivation instead."]),
 ("6. Suspected account compromise", [
  "If a customer reports unauthorised access, such as unknown logins or orders they did not place, ShopEase locks the account "
  "immediately and treats the case as High priority. Customers should also email security@shopease.example. The customer should "
  "reset the password, review recent orders and saved addresses and remove unknown devices. Unauthorised orders are investigated "
  "within 7 days and cancelled or refunded where fraud is confirmed."]),
 ("7. Privacy and personal data", [
  "ShopEase uses personal data to process orders, provide support and prevent fraud, and processes it as required by Indian data "
  "protection law. Customers can request a copy of their data, correction of wrong data or withdrawal of marketing consent. Requests "
  "are answered within 30 days. Customer messages sent to ShopEase may be processed by automated systems, and personal identifiers are "
  "masked before text is shared with external AI providers."]),
 ("8. How to contact support", [
  "Chat support is available 24 hours a day. Phone support is available from 9 AM to 9 PM on 1800-000-0000. Email is "
  "support@shopease.example. Customers can type 'agent' in chat to be connected to a human agent. Customers should quote the order "
  "number and never share passwords, OTPs or card numbers with support."]),
 ("9. Priority levels and response times", [
  "ShopEase classifies every ticket as High, Medium or Low priority. High priority tickets receive a first response within 4 hours "
  "and a target resolution within 2 business days. Medium and Low priority tickets receive a first response within 24 hours, with "
  "resolution targets of 5 business days for Medium and 7 business days for Low.",
  "High priority covers suspected account compromise or fraud, money deducted without an order, duplicate charges, legal or consumer-court "
  "threats and product safety concerns. Medium priority covers upset customers with ordinary issues such as late delivery or refund "
  "delays. Low priority covers general questions."]),
 ("10. Complaint handling process", [
  "Every complaint receives a ticket number and an acknowledgement immediately. The complaint then moves through levels. Level 1 is a "
  "support agent, who aims to resolve it within the target times above. Level 2 is a senior agent or team lead, to whom a complaint moves if "
  "it is not resolved within 3 business days or the customer asks for escalation. Level 3 is the Customer Experience Manager, who decides "
  "within 5 business days. Level 4 is the Grievance Officer at grievance@shopease.example, who acknowledges within 48 hours and resolves "
  "the complaint within 30 days."]),
 ("11. Automatic escalation triggers", [
  ["A High priority ticket with no resolution after 24 hours moves to Level 2.", "A customer contacting support a third time about the same issue moves to Level 2.",
   "A mention of legal action or the consumer court moves to Level 3 within 24 hours.", "A product safety concern moves to Level 3 immediately and the product is placed on hold.",
   "Tickets that the automated triage cannot classify, or classifies with low confidence, are routed to a human agent."]]),
 ("12. Compensation and goodwill", [
  "For service failures such as long delays, agents may offer store credit up to Rs. 500. Team leads may approve up to Rs. 2000 and "
  "the Customer Experience Manager approves higher amounts. Goodwill credit is not a replacement for any refund the customer is owed."]),
 ("13. AI-assisted replies", [
  "ShopEase uses automated tools to classify tickets and to draft replies from these policies. Every drafted reply is reviewed and "
  "approved by a human agent before it is sent. Customers can ask for a human agent at any time."]),
 ("14. Respectful communication", [
  "ShopEase expects respectful communication. Abusive, threatening or discriminatory language towards staff may lead to the "
  "conversation being closed and, for repeated cases, to account restrictions. Customers can also contact the National Consumer "
  "Helpline at 1915 if they feel a complaint was not resolved."]),
])
